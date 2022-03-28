
import random
import time

#----- Version 1 -----#

def pick6():
    
    ticket = []
    
    for x in range(6):
        ticket.append(random.randint(1,99))
        # print(ticket) 
    return ticket

# pick6()

def num_matches(win_tix,tix_in_play):
    
    matches = 0

    for i in range(6):
        if win_tix[i] == tix_in_play[i]:
            matches += 1
    return matches

# num_matches()

match_value = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

num_x_matches = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

win_tix = pick6()

earned = 0
balance = 0
expenses = 0

for i in range(int(100000)):
    tix_in_play = pick6()
    expenses += 2
    balance -= 2
    matches = num_matches(win_tix,tix_in_play)
    num_x_matches[matches] += 1
    earned += match_value[matches]
    balance += match_value[matches]

print('\nWelcome to Pick6!')
print(f'\nYour ticket numbers...')
time.sleep(1) 
print(f'\n{tix_in_play}')
print(f'\nThe winning numbers...')
time.sleep(1)
print(f'\n{win_tix}')
print(f'\nNumber of matches within 100,000 plays...')
time.sleep(2)
print(num_x_matches)
print(f'\nEarnings: {earned}.')
print(f'Balance: {balance}.')

#----- Version 2 -----#

print(f'\nReturn on investiment: {(earned - expenses)/expenses}\n')
