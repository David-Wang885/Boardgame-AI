class Location():
    # Worker placement spot with limits and effects

    def __init__(self):
        self.id = ""
        self.sharable = False
        self.workers = []
        self.reward_coins = 0
        self.reward_vp = 0

    def can_place(self, worker):
        return self.sharable or len(self.workers) == 0

    def place_worker(self, worker):
        pass

    def resolve_effect(self, player):
        pass

    def clear(self):
        self.workers = []

