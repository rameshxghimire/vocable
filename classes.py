"""classes.py
contains Player and Game class definitions.

"""


class Player():
    """blueprint for player objects to be instantiated dynamically.
    
    """
    def __init__(self, name="", word_list=[], pass_taken=0):
        self.name = name
        self.word_list = word_list
        self.pass_taken = pass_taken

    # def add_user(self, name):
    #     """registers the user for the game.
        
    #     :param name: username of the player.
    #     :type name: string
    #     """
    #     self.name = name
    #     return self.name

    # def spell(self, word):
    #     """takes the player's word input and appends it to the word_list.
        
    #     :param word: players valid word input.
    #     :type word: string
    #     """
    #     self.word_list.append(word)
    #     return self.word_list

    # def add_pass_taken(self, pass_taken):
    #     """counts player's passes.
        
    #     :param pass_taken: player passes when not being able to spell a word.
    #     :type pass_taken: int
    #     """
    #     self.pass_taken += pass_taken
    #     return self.pass_taken


class Game():
    """blueprint for game object attributes and functions.
    
    """
    def __init__(self, players=[], status=False):
        # players is a list of dictionaries.
        self.players = players
        self.status = status

    # def player_registration(self, player_data):
    #     """takes player data in dict format and appends in the players list.
        
    #     :param player_data: contains name, word_list and pass_taken as a dictionary for each user.
    #     :type player_data: list
    #     """
    #     self.players.append(player_data)
    #     return self.players













    



