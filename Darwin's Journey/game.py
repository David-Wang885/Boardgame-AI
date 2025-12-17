from turnmanager import *

class Game():
    def __init__(self, players, board, rules):
        self.players = players
        self.board = board
        self.rules = rules
        self.turn_manager = TurnManager
        self.round = 0
        self.max_round = 6
        self.current_player_id = 0

    def start(self):
        pass

    def play(self):
        pass

    def play_round(self):
        pass

    def is_game_over(self):
        pass

    def score_game(self):
        pass

    def get_legal_actions(self,player):
        pass

    def apply_action(self, player, action):
        pass


