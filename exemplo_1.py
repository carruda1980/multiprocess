"""
Primeira etapa do problema

Fazer o download das 100 primeiras imagens dos pokemons da pokeapi

103 Segundos
"""

from datetime import datetime
from os import makedirs
from os.path import exists
from pprint import pprint
from shutil import rmtree, copyfileobj
from urllib.parse import urljoin
from requests import get

path = 'download'
base_url = "https://pokeapi.co/api/v2/"

# Se existir o diretorio apaga o mesmo

if exists(path):
    rmtree(path)
makedirs(path)


# Faz o download e copia para o diretorio
def downloa_file(name, url, * , path=path, type_='png'):
    """Faz o download de um arquivo"""

    response = get(url, stream=True)
    fname = f'{path}/{name}.{type_}'

    with open(fname, 'wb') as f:
        copyfileobj(response.raw, f)

    return fname


# Sprites dos pokemons
def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]


start_time = datetime.now()

# Lista dos 100 primeiros pokemons
pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']

# Sprintes dos 100 primeiros pokemons
images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

files = [downloa_file(name, url) for name, url in images_url.items()]

pprint(files)
pprint(datetime.now() - start_time)

