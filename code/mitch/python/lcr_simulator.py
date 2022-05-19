# LCR Simulator
# Mitch Chapman

from collections import deque
import random
import time
from pprint import pprint

dice_sides = ("L", "C", "R", "dot", "dot", "dot")

print("\nWelcome to the LCR Simulator. This thing will play 'LCR' so you dont have to! (For 2 or more players.)")

game_data = {(input("Please enter a player name: ")):3 for _ in range(2)}

while True:
    user_input = input("Do you have any more players you would like to enter? ('y' or 'n'): ")
    if user_input not in ["y", "n"]:
        print("Invalid input, please try again.")
    elif user_input == "y":
        game_data[input("Please enter a player name: ")] = 3
    else:
        break

game_data["center_pool"] = 0

players = []
for player in game_data:
    if player != "center_pool":
        players.append(player)

players = deque(players)


def score_die(die_face):
    if die_face == "L":
        game_data[players[0]] -= 1
        game_data[players[-1]] += 1
    elif die_face == "R":
        game_data[players[0]] -= 1
        game_data[players[1]] += 1
    elif die_face == "C":
        game_data[players[0]] -= 1
        game_data["center_pool"] += 1
    elif die_face == "dot":
        pass


def only_one_with_chips_check():
    over_zero_chips = []
    for player in players:
        if game_data[player] > 0:
            over_zero_chips.append(player)
    if len(over_zero_chips) == 1:
        return "".join(over_zero_chips)
    else:
        return False

print()
pprint(game_data)

while True:
    person_rolling = players[0]
    print(f"\n{person_rolling} is currently rolling. Outcome below:")
    if game_data[person_rolling] >=3:
        for _ in range(3):
            score_die(random.choice(dice_sides))

    else:
        for _ in range(game_data[person_rolling]):
            score_die(random.choice(dice_sides))
    
            
    if only_one_with_chips_check():
        pprint(game_data)
        print(f"\n{only_one_with_chips_check()} has won the game!!!!!!!")
        their_chips = game_data[only_one_with_chips_check()]
        center_chips = game_data["center_pool"]
        print(f"They had {their_chips} chips and picked up {center_chips} chips from the center of the table.")
        break
    
    pprint(game_data)
    time.sleep(0.7)
    players.rotate(-1)
        








