'''
PDX Code Guild - Class Koi
Lab 06 - Pick6
Matt Walsh
'''

 
# Version 1
""" 
from random import randint

# list of prize values
prizes = [0,4,7,100,50000,1000000,25000000]

# starting balance of player
balance = 0

# number of tickets purchased by player
num_tickets = 100000

# function to generate tickets
def pick6():
    ticket = []
    for x in range(6):
        ticket.append(randint(1,99))
    return ticket

# save winning ticket to list
winning = pick6()

# find number of matches 
def num_matches(winning,player):
    # variable to hold number of matching digits
    matches = 0
    # iterate through numbers on tickets to find matches
    for x in range(6):
        if winning[x] == player[x]:
            matches += 1
    return matches

# adjust balance based on number of matches
def adjust_balance(matches):
    balance_change = prizes[matches] - 2
    return balance_change

# display money properly
def process_balance(balance):
    # empty string for processed balance
    processed_balance = ''
    # if balance is less than 0, add '-' to string
    if balance < 0:
        processed_balance += 'lost '
    else:
        processed_balance += 'won '
    # convert absolute value of balance to string separated by commas
    balance = '{:,}'.format(abs(balance))
    # add dollar sign and balance to string
    processed_balance += '$' + balance
    return processed_balance

# check tickets and adjust balance based on matches
for x in range(num_tickets):
    matches = num_matches(winning,pick6())
    balance += adjust_balance(matches)

# display results
print(f'After playing {"{:,}".format(num_tickets)} times, you {process_balance(balance)}.')
"""


# Version 2

from random import randint

# list of prize values
prizes = [0,4,7,100,50000,1000000,25000000]

# starting balance and amount spent of player
balance = 0
spent = 0
winning_tickets = 0

# function to generate tickets
def pick6():
    ticket = []
    for x in range(6):
        ticket.append(randint(1,99))
    return ticket

# save winning ticket to list
winning = pick6()

# find number of matches 
def num_matches(winning,player):
    # variable to hold number of matching digits
    matches = 0
    # iterate through numbers on tickets to find matches
    for x in range(6):
        if winning[x] == player[x]:
            matches += 1
    return matches

# adjust balance based on number of matches
def adjust_balance(matches):
    balance_change = prizes[matches]
    return balance_change

# display money properly
def process_balance(balance):
    # empty string for processed balance
    processed_balance = ''
    # # convert absolute value of balance to string separated by commas
    # balance = '{:,}'.format(abs(balance))
    # add dollar sign and balance to string
    processed_balance += '$' + '{:,}'.format(abs(balance))
    return processed_balance

# Ask user how many times they would like to play
while True:
    num_tickets = input('How many tickets would you like to buy? ')
    try:
        num_tickets = int(num_tickets)
        break
    except:
        print('Please enter a number with only digits.')

# check tickets and adjust balance based on matches
for x in range(num_tickets):
    matches = num_matches(winning,pick6())
    if matches > 0:
        winning_tickets += 1
    balance += adjust_balance(matches)
    spent += 2

# add "ticket"/"tickets" to winning_tickets
if winning_tickets == 1:
    winning_tickets = '{:,}'.format(winning_tickets) + ' ticket'
else:
    winning_tickets = '{:,}'.format(winning_tickets) + ' tickets'

# display results
print(f'''
After playing {"{:,}".format(num_tickets)} times:
- you spent {process_balance(spent)}
- you won {process_balance(balance)}
- {winning_tickets} had at least one match

In total, you {"lost" if balance - spent < 0 else "won"} \
{process_balance(balance - spent)}.
Your ROI for this session is {round((balance - spent)/spent,2)}
''')