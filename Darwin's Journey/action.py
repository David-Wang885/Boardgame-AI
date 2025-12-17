class Action:
    # Uniform interface for all actions.
    def __init__(self):
        self.player_id = None

    def is_legal(self, game, player):
        pass

    def apply(self, game, player):
        pass

class PlaceWorkerAction(Action):
    def __init__(self):
        super().__init__()

    def is_legal(self, game, player):
        pass

    def apply(self, game, player):
        pass


class TravelAction(Action):
    def __init__(self):
        super().__init__()

    def is_legal(self, game, player):
        pass

    def apply(self, game, player):
        pass

