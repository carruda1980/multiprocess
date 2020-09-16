from shutil import copyfileobj
from requests import get
from os import makedirs
from os.path import exists
from shutil import rmtree


path = 'download'
if exists(path):
    rmtree(path)
makedirs(path)


def get_file_bin(args):
    """Faz o download do binario"""
    name, url = args
    return name, get(url, stream=True).raw


# Sprites dos pokemons
def get_sprite_url(url, sprite='front_default'):
    """Pega a url do sprite"""
    return url['name'], get(url['url']).json()['sprites'][sprite]


# Salva o arquivo no diretorio
def save_file(args, path=path, type_='png'):
    """Salva um arquivo arquivo"""

    name, binary = args
    fname = f'{path}/{name}.{type_}'
    with open(fname, 'wb') as f:
        copyfileobj(binary, f)

    return fname


def pipeline(*funcs):
    def inner(argument):
        state = argument
        for func in funcs:
            state = func(state)

    return inner

target = pipeline(get_sprite_url, get_file_bin, save_file)



