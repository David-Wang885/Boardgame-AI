from worker import *
from resources import *

class Player():
    # Holds everything belonging to a player

    def __init__(self):
        self.id = 0
        self.workers = [Worker]
        self.vp = 0
        self.resource = Resources