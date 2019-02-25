"""vocable.py
contains the game logic, ui and other elements.

"""

import sys
import datetime

from classes import Player
from classes import Game


# record start time
playtime = datetime.datetime.now()


# function to initiate the welcome screen
def welcome_screen():
    # welcome statement
    print(f"""
    -----***** Welcome to VOCABLE *****-----
    Current time: {playtime}
    
    Respect your opponent & enjoy the game!

    """)


# function to ask the number of players
def take_player_number():
    """decides player number for registration
    
    :return: player_number
    :rtype: int
    """
    invalid_number = True
    player_number = 0
    while invalid_number:
        try:
            player_number = int(input("How many players are you (min. 2)? "))
            if player_number >= 2:
                invalid_number = False
                return player_number
            else:
                invalid_number = True
                print("\nOnly 2 or more people can play this game.")
                continue
        except ValueError:
            print("\nDid you enter a valid number?\nI guess not. Please enter a valid number.\n")
            continue

# create a player_list list to hold player names
# before we convert them into Player objects
player_list = []
players_data = []


# function to create a list of players
def create_player_list(player_number):
    """instantiate Player objects as many as player_number
    
    :param player_number: return value from take_player_number() function.
    :type player_number: int
    """
    global player_list
    for num in range(player_number):
        _ = input(f"what is the name of player {num + 1}: ")
        player_list.append(_)
    return player_list


# function to create player objects for players in the list
def create_player_objects(player_list):
    """creates Player objects for each names in player_list and puts them in a new list.
    
    :param player_list: list containing player names.
    :type player_list: list
    """
    global players_data
    players_data = [Player(name) for name in player_list]
    return players_data


# the main game logic
def game_logic(players_data):
    """takes in players data and initiates the game logic.
    
    :param players_data: contains Player objects with name, word_list and pass_taken as attributes.
    :type players_data: list containing dictionaries as items.
    """
    # Initialise allowed and prohibited words from external file read.
    with open("docs/wordDict.txt", "r") as wordDict:
        allowed_words = wordDict.read()
    with open("docs/excludeWords.txt", "r") as excludeWords:
        prohibited_words = excludeWords.read()
    game_switch = True
    valid_word = False
    player_turn = ""
    start_letter = ""
    while game_switch:
        player_turn = players_data[0].name
        if not players_data:             # iff empty list
            print("Something went wrong. I could not find players! Please restart the game.")
            break
        elif len(players_data) == 1:        # when one person is left
            print(f"\n{players_data[0].name.upper()} wins.\nCongratulations!\n°°*°°*°°*°°*°°*°°*° ")
            print(f"beat all opponents in: {(datetime.datetime.now() - playtime).total_seconds()} seconds\n°°*°°*°°*°°*°°*°°*°\n")
            break
        else:
            print(f"\nIt is {player_turn.upper()}'s turn")
            # add a copy of first element to the end
            players_data.append(players_data[0])
            # remove the first element. so that next turn is next ones'.
            players_data.remove(players_data[0])
            # start the game
            while not valid_word:
                if not start_letter:
                    input_word = input(f"please enter a valid word to begin: ")
                    if input_word.lower() in allowed_words and input_word.lower() not in prohibited_words:
                        players_data[-1].word_list.append(input_word)
                        start_letter = input_word[-1].upper()
                        print(f"\nStarting letter for next player is: {start_letter}")
                        break
                    else:
                        players_data[-1].pass_taken += 1
                        print(f"\n!!¡¡ FOUL¡¡!!!!¡¡ FOUL¡¡!!!!¡¡ FOUL¡¡!!\nThe word was not recognised as a valid word.\nPenalty: 1 pass({3 - players_data[-1].pass_taken} left)\n")
                        print("Turn goes to your opponent.")
                        valid_word = False
                        if players_data[-1].pass_taken >= 3:
                            print(f"LOST!\n{players_data[-1].name.upper()} is out of the game")
                            players_data.pop()
                            continue
                else:
                    input_word = input(f"please enter a valid word begining with letter {start_letter}: ")
                    if input_word.lower() in allowed_words and input_word.lower() not in prohibited_words and input_word[0].upper() == start_letter:
                        players_data[-1].word_list.append(input_word)
                        start_letter = input_word[-1].upper()
                        print(f"\nStarting letter for next player is: {start_letter}")
                        break
                    else:
                        players_data[-1].pass_taken += 1
                        print(f"\n!!¡¡ FOUL¡¡!!!!¡¡ FOUL¡¡!!!!¡¡ FOUL¡¡!!\nThe word was not recognised as a valid word.\nPenalty: 1 pass({3 - players_data[-1].pass_taken} left)\n")
                        print("Turn goes to your opponent.")
                        valid_word = False
                        if players_data[-1].pass_taken >= 3:
                            print(f"LOST!\n{players_data[-1].name.upper()} is out of the game")
                            players_data.pop()
                        break


# show the welcome screen
welcome_screen()

# ask number of players
player_number = take_player_number()

# create a list of players
create_player_list(player_number)

# instantiate Player objects
create_player_objects(player_list)

# initiate the game logic
if __name__ == "__main__":
    game_logic(players_data)
