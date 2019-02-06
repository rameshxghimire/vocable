""" game.py
    contains game related classes.
"""


class Game(object):

    def __init__(self, num_players=[], player_names=[]):
        self.num_players = num_players
        self.player_names = player_names
    
    def welcome_screen(self):
        print("""
        _______________________________________________
        **********----------VOCABLE----------**********
        -----------------------------------------------
        *********-----Welcome to VOCABLE!-----*********
        ===============================================
        """)
    
    def player_registration(self):
        # update the number of players
        self.num_players = int(input("How many players?: "))
        return self.num_players
    
    def player_list(self, num_players, take_player_names=""):
        if self.num_players >= 2:
            for idx in range(self.num_players):
                self.take_player_names = input(f"What is the name of player {idx + 1}: ")
                self.player_names.append(self.take_player_names)
            return self.player_names
        else:
            print("There must be at least 2 players. Adios, try some other game!")

# ? test the functions
# game1 = Game()
# game1.welcome_screen()
# game1.player_registration()
# num_players = game1.num_players
# print(game1.num_players)
# game1.player_list(num_players)
# print(game1.player_names)

# TODO : turn rotating logic (see -> cycle)
# TODO : game win, feedback etc.
# TODO : ux enhancements
