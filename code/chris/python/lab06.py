'''
Lab 6: Pick6
Lottery Simulator/Investment Calculator
'''

import random

winning_numbers = []
player_numbers = {}
match_count = 0
sim_count = 100000
balance = 0
expenses = 0
earnings = 0

payouts = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

def pick6(): # returns a tuple of six numbers (order matters)
    six_numbers = []
    for i in range(6):
        six_numbers.append(random.randint(1, 99))
    return tuple(six_numbers)

def num_matches(winning_ticket, ticket): # returns the number of matches between the winning ticket and other ticket
    matches = 0
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matches += 1
    return matches

winning_numbers = pick6()

for n in range(sim_count): # generate a dictionary of lottery tickets
    player_numbers[n] = pick6()
    
    expenses += 2

    match_count = num_matches(winning_numbers, player_numbers[n]) # find the number of matches on ticket

    ticket_winnings = payouts[match_count]

    earnings += ticket_winnings

balance += earnings - expenses
return_on_investment = ((earnings - expenses) / expenses) * 100

print(f'\nCongratulations on your recent investment in {sim_count} lottery tickets.\nThe following is your investment analysis:\n')
print(f'Account Balance: ${balance}\nTotal Earnings: ${earnings}\nReturn on Investment (ROI): {return_on_investment}%\n')
