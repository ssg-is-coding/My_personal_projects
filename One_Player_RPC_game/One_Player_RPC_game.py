# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:10:55 2026

@author: sandh
"""
from random import randint
from matplotlib import pyplot as plt



def init_choice_list(handshapes):
    k = 0;
    while k < 100:
        if k <= 33:
            handshapes.append(0)
            k += 1
        elif k >= 33 and k <= 66:
            handshapes.append(1)
            k += 1
        else:
            handshapes.append(2)
            k += 1
    return handshapes

def adapt_bot_decision(choice_list, indice, choice):
    if choice == 0:
        choice_list[indice] = 1
    elif choice == 1:
        choice_list[indice] = 2
    else:
        choice_list[indice] = 0
    return choice_list
    
def handshape_translation(handshape_code):
    if handshape_code == 0:
        return "pierre"
    elif handshape_code == 1:
        return "feuille"
    elif handshape_code == 2:
        return "ciseaux"
    else:
        print(f"Code Error : {handshape_code} unknown", handshape_code)
        return ""
    

def main_game():
    valid_commands = ["pierre", "feuille", "ciseaux", "exit", "score"]
    valid_shapes = ["pierre", "feuille", "ciseaux"]
    num_of_tests = 10000
    tests_choices = [valid_shapes[randint(0, 2)] for l in range(num_of_tests)]
    handshapes = []
    player_score_track = []
    bot_score_track = []
    played_games_track = []
    init_choice_list(handshapes)
    player_score = 0
    bot_score = 0
    played_games = 0
    #while(True)
    for k in range(num_of_tests):
        if played_games % 2 == 0:
            player_score_track.append(player_score)
            bot_score_track.append(bot_score)
            played_games_track.append(played_games)
            if len(played_games_track) > 0:
                plt.plot(player_score_track,"red", marker = 'o')
                plt.plot(bot_score_track,"blue", marker = 'o')
                plt.show()
        player_hand = tests_choices[k]#str(input("enter the handshape : "))
        if player_hand not in valid_commands:
            print(f"Command Error : {player_hand} is not a valid command")
            continue
        if player_hand == "exit":
            break
        if player_hand == "score":
            print(f"Player_score : {player_score}")
            print(f"Bot_score : {bot_score}")
            continue
        bot_choice_idx = randint(0, 99)
        real_choice = handshape_translation(handshapes[bot_choice_idx])
        print(f"Bot chose: {real_choice}")

        if player_hand == real_choice:
            print("Egalité !")
        elif (player_hand == "pierre" and real_choice == "feuille") or \
             (player_hand == "feuille" and real_choice == "ciseaux") or \
             (player_hand == "ciseaux" and real_choice == "pierre"):
            print("Bot won !")
            bot_score += 1
            played_games += 1
        else:
            print("Player won !")
            player_score += 1
            played_games += 1
            mapping = {"pierre": 0, "feuille": 1, "ciseaux": 2}
            adapt_bot_decision(handshapes, bot_choice_idx, mapping[player_hand])
    print(f"Player score : {player_score}")
    print(f"Bot score : {bot_score}")
         
             
        