from urllib.parse import urljoin
from threading import Event
from queue import Queue
from requests import get

base_url = "https://pokeapi.co/api/v2/"
event = Event()
fila = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=5')).json()['results']
    [fila.put(pokemon) for pokemon in pokemons]
    event.set()
    fila.put('Kill')
    import ipdb; ipdb.set_trace()

get_urls()