class Resources():
    # Encapsulate player resources

    def __init__(self):
        self.coins = 0
        self.specimen = []
        self.evolution = 1
        self.tent = 5
        self.stamp = [4, 4, 4]
        self.objective = {"gold": [], "silver": [], "none": []}
        self.lens = 6

    def gain_coins(self, coins):
        pass

    def gain_specimen(self, specimen):
        pass

    def gain_evolution(self, evolution):
        pass

    def gain_objective(self, objective):
        pass

    def can_pay(self, coins):
        pass

    def pay(self, coins):
        pass

    def put_tent(self):
        pass

    def put_stamp(self):
        pass

    def put_lens(self):
        pass
