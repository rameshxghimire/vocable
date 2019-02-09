"""Main file with game logic.

"""
from itertools import cycle
from players import Players
from game import Game


# create game instance
game = Game()

# show the welcome screen
game.welcome_screen()

# # register the players
# number of players
num_players = game.player_registration()
# players' list of names
player_names = game.player_list(num_players)

# decide whose turn it is
# updates the list, current turn item is sent to the end of the list
game.player_turns_decider(player_names)

# assign player objects on registered player names
# intention: values of player names should be Player objects
user_registry = {name: Players(name) for name in player_names}

# let the game begin
# last items are the keys of the dictionary
# first run
user_registry[player_names[-1]].start_game()
# game.player_turns_decider(player_names)  # define the next turn
# print(user_registry[player_names[-2]].start_game())

def user_turn():
    turns = next(cycle(user_registry))
    print(f"It\'s {turns}\'s turn now.")




