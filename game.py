""" game.py
    contains game related classes.
"""


class Game(object):

    def __init__(self, num_players=[], player_names=[], spelled_words=[], start_letter="", condition=True, winner=False):
        self.num_players = num_players
        self.player_names = player_names
        self.spelled_words = spelled_words
        self.condition = condition
        self.start_letter = start_letter
        self.winner = winner
    
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

    def player_turns_decider(self, player_names):
        self.player_turn = self.player_names[0]
        print(f"\nIt is {self.player_turn}'s turn")
        self.player_names.append(self.player_names[0])
        self.player_names.remove(self.player_names[0])
        return self.player_names
    
    def start_letter_setter(self, start_letter=""):
        self.start_letter = start_letter
        return start_letter

    def game_loop(self, spelled_words=[], condition=True):
        # open dictionaries for word validation
        with open("docs/wordDict.txt", "r") as wordDict:
            allowedWords = wordDict.read()
        with open("docs/excludeWords.txt", "r") as excludeWords:
            notAllowedWords = excludeWords.read()
        # initiate valid word flaf
        self.valid_word = False
        # start the game loop
        while self.condition:
            while not self.valid_word:
                self.spell_your_word = input(f"\nType your word starting with the letter {self.start_letter}\nIf you want to pass, type \"pass\": ")
                if self.spell_your_word.lower() in allowedWords and self.spell_your_word.lower() not in notAllowedWords:
                    if self.spell_your_word[-1].upper() == self.start_letter:
                        self.spelled_words = spelled_words.append(self.spell_your_word)
                        self.start_letter = self.spell_your_word.upper()[-1]
                        # self.valid_word = True
                        return self.start_letter
                    elif self.spell_your_word.lower() == "pass":
                        return (f"\nPass taken.\nTurn goes to your opponent\n")
                    else:
                        return (f"\nNot a valid entry. You needed to start with {self.start_letter}.\nurn goes to your opponent\n")
                else:
                    self.valid_word = False
                    print("\nNot a valid word. Be civil, use dictionary words & Try again!")
                    continue
            continue



# ? test the functions
# game1 = Game()
# game1.welcome_screen()
# game1.player_registration()
# num_players = game1.num_players
# print(game1.num_players)
# game1.player_list(num_players)
# print(game1.player_names)
# game1.player_turns_decider(game1.player_names)
# print(game1.player_names)
# game1.start_letter_setter("E")
# game1.game_loop()
# ! pass, works
