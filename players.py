"""
players.py

contains required classes and objects.

"""


class Players(object):
    """Define player character and associated functions.
    """
    starting_word = None
    next_start_let = None
    pass_taken = 0

    def __init__(self, name, turn=False):
        self.name = name
        self.turn = turn

    def setTurn(self):
        self.turn = True
    
    def start_game(self):
        """This function is executed one time per game at the start.
        
        Returns
        -------
        String
            A single letter if the input word is allowed dictionary word.
            Warning if the word is not allowed.
        """

        global starting_word
        global next_start_let
        starting_word_flag = False

        # Initialise allowed and restricted words from external file read.
        with open("docs/wordDict.txt", "r") as wordDict:
            allowedWords = wordDict.read()
        with open("docs/excludeWords.txt", "r") as excludeWords:
            notAllowedWords = excludeWords.read()

        # Take user input is the starting_word_flag is default False
        while not starting_word_flag:
            starting_word = input("\nChose a valid word to start the game: ")
            # Verify that the input word is valid
            if starting_word.lower() in allowedWords and starting_word.lower() not in notAllowedWords:
                starting_word_flag = True
                next_start_let = starting_word.upper()[-1]
                return next_start_let
            else:
                starting_word_flag = False
                print("\nNot a valid word. Be civil, use dictionary words & Try again!")
                continue

    def spell_your_word(self, first_letter):
        self.first_letter = first_letter
        global pass_taken
        pass_taken = 0
        word_input = input(f"\nEnter a word starting with the {first_letter},\nIf you want to pass, type \"pass\": ")
        if word_input.lower() != "pass" and word_input.lower()[0] == first_letter:
            next_start_let = word_input.upper()[-1]
            return next_start_let
        elif word_input.lower() != "pass" and word_input.lower()[0] != first_letter:
            print(f"\nNot a valid entry. You needed to start with {first_letter}.\nPENALTY POINT TAKEN: 1 PASS ADDED")
            pass_taken += 1
            if pass_taken == 3:
                return f"You have no pass left. You lost the game, LOSER!"
            else:
                return f"\nPass taken = {pass_taken}/3.\n{3 - pass_taken} passes left.\n\nTurn goes to your opponent\n"
        else:
            pass_taken += 1
            if pass_taken == 3:
                return f"You have no pass left. You lost the game, LOSER!"
            else:
                return f"Pass taken = {pass_taken}/3.\n{3 - pass_taken} passes left.\nTurn goes to your opponent"
# Testing
# rg = Players("PL1")
# print(rg.start_game())
# print(rg.spell_your_word(next_start_let))
# print(rg.name)
# print(rg.pass_taken)
