from time import sleep
from urllib.parse import urljoin
from threading import Event, Thread
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
    #import ipdb; ipdb.set_trace()


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super.__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False

        print(self.name, 'Started')

    def run(self):
        #event.wait()

        while not self.queue.empty():
            pokemon = self.queue.get()
            print(self.name, pokemon)

            if pokemon == "Kill":
                self.queue.put(pokemon)
                self._stoped = True
                break

            self._target(pokemon)

    def join(self):
        while not self._stoped:
            sleep(0.1)

            
get_urls()