from game import *

game = Game(players, board, rules)

game.start()

while not game.is_game_over():
    player = game.turn_manager.next_player()
    actions = game.get_legal_actions(player)
    action = player.controller.choose_action(game, player)
    game.apply_action(player, action)

game.score_game()

