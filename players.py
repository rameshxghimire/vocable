"""
players.py

contains required classes and objects.

"""


class Players(object):

    def __init__(self, name):
        self.name = name
        self.turn = turn
        turn = False

    def setTurn(self, turn=True):
        self.turn = True

    def getTurn(self):
        return self.turn
    

class Game(object):
    
    def __init__(self, current_player):
        self.current_player = current_player
        self.lose = lose
        lose = False

    def start_game(self):
        starting_word = input("Chose a word to start the game: ")
        return starting_word.upper()[-1]

    def spell_your_word(self, first_letter):
        self.first_letter = first_letter
        pass_taken = 0
        word_input = input(f"""enter a word starting with the {first_letter}, /n
                            If you want to pass, type: pass""")
        if word_input.lower == "pass":
            pass_taken += 1
        else:
            return word_input.upper()[-1]

