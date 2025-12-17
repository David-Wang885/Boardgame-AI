class Location():
    # Worker placement spot with limits and effects

    def __init__(self):
        self.id = ""
        self.capacity = 1
        self.workers = []
        self.reward_coins = 0
        self.reward_vp = 0

    def is_full(self):
        pass

    def can_place(self, worker):
        pass

    def place_worker(self, worker):
        pass

    def resolve_effect(self, player):
        pass

    def clear(self):
        pass

