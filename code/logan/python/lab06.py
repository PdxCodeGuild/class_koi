## Versions 1 & 2 ##
## Code ##

import random

# Some variables
balance = 0
total_expenses = 0
total_earnings = 0

# Functions

def payout(x):
# This determines the payout based on how many matches the player got.
    if x == 0:
        return (0)
    elif x == 1:
        return (4)
    elif x == 2:
        return (7)
    elif x == 3:
        return (100)
    elif x == 4:
        return (50000)
    if x == 5:
        return (1000000)
    if x == 6: 
        return (25000000)



def pick6():
# This is used to set the player ticket and dealer ticket.
    ticket = []
    for i in range(0,6):
        selection = str(random.randint(1, 99))
        ticket.append(selection)
    return ticket

# This determines the number of matches between the player and dealer ticket
def num_matches(tick1, tick2):
    matchset = []
    for x in tick1:
        comp_val = tick1.index(x)
        if x == tick2[comp_val]:
            matchset.append(1)
    return len(matchset)

def roi(earnings, expenses):
# This determines ROI
    return (earnings - expenses) / expenses

while True:
    try:
        how_many = int(input("\nHow many times would you like to play?..."))
        break
    except:
        print("Invalid input.  Please input a number as a digit.")

# Does all necessary ops as many times as the user wanted.

for cycles in range (0,how_many):
    balance -= 2
    total_expenses += 2
    your_ticket = pick6()
    dealer_ticket = pick6()
    result = num_matches(your_ticket, dealer_ticket)
    purse = payout(result)
    total_earnings += purse
    print(f"\nNumber of matches: {result}.")
    print(f"Purse after ticket cost: {purse}.")
    balance += purse

# Output

print(f"""
Your career earnings: {balance}.
Your ROI: {roi(total_earnings, total_expenses)}.
""")

# Dang...it's hard to win the lottery. :(

