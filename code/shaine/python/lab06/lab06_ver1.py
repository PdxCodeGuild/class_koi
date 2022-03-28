import random

#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#      Lab 6: Pick 6
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# Initially the program will pick 6 random numbers as the 'winner'. 
# Then try playing pick6 100,000 times

def pick6():
    """
    return a list of 6 random numbers
    """
    num_list = []

    while len(num_list) < 6:
        num = random.randint(0, 100)
        if num not in num_list:
            num_list.append(num)

    return num_list


def num_matches(winning_ticket, ticket):
    """
    return the number of matches between the 2 tickets
    """
    ... # use index positons to verify matches

    matches = 0
    for  i in range (0, 6):
        if winning_ticket[i] ==  ticket[i]:
            matches += 1

    return matches



tickets = 0
winnings = 0
total_matches = 0

while tickets < 100000:

    winning_ticket = pick6()
    ticket = pick6()    

    matches = num_matches(winning_ticket, ticket)
    total_matches += matches

    if matches > 0:
        if matches == 1:
            winnings += 4
 
        elif matches == 2:
            winnings += 7
        
        elif matches == 3:
            winnings += 100

        elif matches == 4:
            winnings += 50000

        elif matches == 5:
            winnings += 1000000

        elif matches == 6:
            winnings += 25000000
    tickets += 1

ticket_cost = tickets*2
balance = (winnings - ticket_cost)

print(f"{tickets} tickets had {total_matches} matches and a winnings balance of ${balance}")

