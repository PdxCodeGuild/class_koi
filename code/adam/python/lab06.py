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

winning_ticket = pick6() # winning_ticket = pick6(nums)
ticket = pick6() # purchased ticket

# function to check winning ticket and purchased ticket
def num_matches(winning_ticket, ticket):
    matches = 0
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matches += 1
    return matches

# winning_ticket = [1,2,3,4,5,6]
# ticket = [1,2,3,4,5,6]

print(winning_ticket)
print(ticket)
print (num_matches(winning_ticket, ticket))





