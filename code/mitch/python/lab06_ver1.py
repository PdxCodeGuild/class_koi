# Lab 6: Pick6
# Version 1
# Mitch Chapman

import random

payouts_for_matches = {
    "0": 0,
    "1": 4,
    "2": 7,
    "3": 100,
    "4": 50000,
    "5": 1000000,
    "6": 25000000,
}

num_of_winning_tickets = 0
balance = 0

number_list = [num for num in range(1, 100)]


def pick6():
    """return a list of 6 random numbers"""
    return random.sample(number_list, 6)


def num_matches(winning_ticket, ticket):
    """return the number of matches between the 2 tickets"""
    match_count = 0
    for inx, num in enumerate(winning_ticket):
        if ticket[inx] == num:
            match_count += 1
    return match_count

    
winning_numbers = pick6()


for _ in range(100000):
    ticket_numbers = pick6()
    balance -= 2

    matches = (num_matches(winning_ticket=winning_numbers, ticket=ticket_numbers))
    
    if matches:
        num_of_winning_tickets += 1
    
    balance += payouts_for_matches[str(matches)]


print(f"""
      ****** This gambling simulator just played the 'Pick Six' lottery 100,000 times. ******
      
      There were {num_of_winning_tickets} winning tickets.
      Starting at $0.00, the final balance after 100,000 games is:  ${"{:.2f}".format(balance)}
      """
)























