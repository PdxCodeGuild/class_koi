'''
PDX Code Guild - Class Koi
Optional Lab - LCR Simulator
Matt Walsh
'''

from random import randint as rand

while True: # ask for number of chips to play with and validate entry
    num_chips = input('How many chips is everyone starting with? ')
    try:
        num_chips = int(num_chips)
        if num_chips < 1:
            print('You need more chips than that! Try again.')
        else:
            break
    except:
        print('Please enter your answer as a number.')

player_list = [] # empty list to store names and chips

while True: # ask how many players are playing, validate entry, and add each player to the list with starting chips
    num_players = input('How many players are there? ')
    try:
        num_players = int(num_players)
        i = 1
        while i <= num_players:
            player_name = input(f'Please enter players {i}\'s name: ')
            player_list.append([player_name, num_chips])
            i += 1
        break
    except:
        print('Please enter your answer as a number.')



'''
throw dice - forgot to add multiple throws per player/based on number of chips
---dice options are 1:l 3:c 5:r

do dice evaluation and chip adjustment

check for number of players with non-zero chip totals
    if > 0 keep playing
    if == 1 stop, declare winner

'''


players_with_chips = num_players
current_player = 0

while True:
    while players_with_chips > 1:
        right_player = current_player - 1
        if current_player + 1 > num_players - 1:
            left_player = current_player - num_players + 1
        else:
            left_player = current_player + 1
        throw = rand(1,6) # throw dice
        print(throw) ##### debug, delete later #####
        if throw == 1:
            player_list[current_player][1] -= 1
            player_list[left_player][1] += 1
            print(player_list) ##### debug, delete later #####
        elif throw == 3:
            player_list[current_player][1] -= 1
            print(player_list) ##### debug, delete later #####
        elif throw == 5:
            player_list[current_player][1] -= 1
            player_list[right_player][1] += 1
            print(player_list) ##### debug, delete later #####
        current_player = left_player
        players_with_chips = 0
        for player in player_list:
            print(player) ##### debug, delete later #####
            if player[1] > 0:
                players_with_chips += 1
    break
    
print(player_list) ##### debug, delete later #####
print(players_with_chips) ##### debug, delete later #####