# Lab 06 - Pick 6
# Program to pick 6 numbers check against winning numbers loop many times

# import random module

import random
# create list of numbers 1-99
# nums = list(range(1,100))

# funtion to pick 6 random numbers from 1-99 without duplicates
def pick6():
     # use random shuffle module to shuffle list
    nums = list(range(1,100))
    random.shuffle(nums)
    temp_ticket = nums[:7]
    return temp_ticket

# function to check winning ticket and purchased ticket
def num_matches(winning_ticket, ticket):
    matches_temp = 0
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matches_temp += 1
    return matches_temp

winnings_dict = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000,
}

# winning_ticket = [1,2,3,4,5,6]
# ticket = [1,2,3,4,5,6]
# print(winning_ticket)
# print(ticket)
# print (num_matches(winning_ticket, ticket))
# matches = num_matches(winning_ticket, ticket)
# print(f'${winnings_dict[matches]}')

i = 0
while i < 10:
    i =+ 1
    cost = 0
    winning_ticket = pick6() # winning_ticket = pick6(nums)
    ticket = pick6() # purchased ticket
    matches = num_matches(winning_ticket, ticket)
    winnings = winnings_dict[matches]
    cost = cost - 2 + winnings
    print(winning_ticket)
    print(ticket)
    print(matches)
