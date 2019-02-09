"""
players.py

contains required classes.

"""


class Players(object):
    """Define player character and associated functions.
    """
    def __init__(self, name, next_start_let=None, word_input="", pass_taken=0):
        self.name = name
        self.next_start_let = next_start_let
        self.pass_taken = pass_taken
    
    def start_game(self):
        """This function is executed one time per game at the start.
        
        Returns
        -------
        String
            A single letter if the input word is allowed dictionary word.
            Warning if the word is not allowed.
        """
        self.starting_word_flag = False
        self.starting_word = ""
        # Initialise allowed and restricted words from external file read.
        with open("docs/wordDict.txt", "r") as wordDict:
            allowedWords = wordDict.read()
        with open("docs/excludeWords.txt", "r") as excludeWords:
            notAllowedWords = excludeWords.read()

        # Take user input if the starting_word_flag is default/False
        while not self.starting_word_flag:
            self.starting_word = input("\nChose a valid word to start the game: ")
            # Verify that the input word is valid
            if self.starting_word.lower() in allowedWords and self.starting_word.lower() not in notAllowedWords:
                self.starting_word_flag = True
                self.next_start_let = self.starting_word.upper()[-1]
                return self.next_start_let
            else:
                self.starting_word_flag = False
                print("\nNot a valid word. Be civil, use dictionary words & Try again!")
                continue

    def spell_your_word(self, next_start_let):
        self.word_input = input(f"\nEnter a word starting with the {self.next_start_let},\nIf you want to pass, type \"pass\": ")
        if self.word_input.lower() != "pass" and self.word_input.lower()[0] == self.next_start_let:
            self.next_start_let = self.word_input.upper()[-1]
            return self.next_start_let
        elif self.word_input.lower() != "pass" and self.word_input.lower()[0] != self.next_start_let:
            print(f"\nNot a valid entry. You needed to start with {self.next_start_let}.\nPENALTY POINT TAKEN: 1 PASS ADDED")
            self.pass_taken += 1
            if self.pass_taken == 3:
                return f"You have no pass left. You lost the game, LOSER!"
            else:
                return f"\nPass taken = {self.pass_taken}/3.\n{3 - self.pass_taken} passes left.\n\nTurn goes to your opponent\n"
        else:
            self.pass_taken += 1
            if self.pass_taken == 3:
                return f"You have no pass left. You lost the game, LOSER!"
            else:
                return f"Pass taken = {self.pass_taken}/3.\n{3 - self.pass_taken} passes left.\nTurn goes to your opponent"
# Testing
# rg = Players("PL1")
# print(rg.start_game())
# print(rg.spell_your_word(next_start_let))
# print(rg.name)
# print(rg.pass_taken)
