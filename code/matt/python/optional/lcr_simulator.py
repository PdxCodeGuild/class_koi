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

players_with_chips = num_players # set the initial number of players with chips to the total number of players
current_player = 0 # set the starting player
throw = [] # empty list to hold dice throws

while True:
    while players_with_chips > 1: # continue looping as long as more than 1 player has chips
        right_player = current_player - 1 # create variable as alias for player to the right
        if current_player + 1 > num_players - 1: # create variable as alias for player to the left, avoiding index errors
            left_player = current_player - num_players + 1
        else:
            left_player = current_player + 1
        
        # throw dice up to 3 times based on number of chips in hand
        for x in range(player_list[current_player][1] if player_list[current_player][1] <3 else 3):
            throw.append(rand(1,6))

        # adjust chip totals based on throw - "1" = "L", "3" = "C", "5" = "R"
        for x in throw:
            if x == 1:
                player_list[current_player][1] -= 1
                player_list[left_player][1] += 1
            elif x == 3:
                player_list[current_player][1] -= 1
            elif x == 5:
                player_list[current_player][1] -= 1
                player_list[right_player][1] += 1

        throw.clear() # empty throw list for use next loop

        current_player = left_player # set current player to player to the left for next loop

        # clear player_with_chips variable, then recalculate from player_list
        players_with_chips = 0
        for player in player_list:
            if player[1] > 0:
                players_with_chips += 1
    
    # once higher loop clears when only 1 player has chips, find and declare winner.
    for player in player_list:
        if player[1] > 0:
            print(f'\nThe winner is {player[0]} with {player[1]} {"chips" if player[1] > 1 else "chip"}!\n')

    # allow player to continue or quit
    quit = input('Would you like to play again? Enter "Y" to continue: ')
    if quit.upper() != "Y":
        print('Goodbye!')
        break
