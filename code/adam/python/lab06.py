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
# winning_ticket = pick6(nums)
winning_ticket = pick6()
ticket = pick6()
def num_matches(winning_ticket, ticket):
    i = 0
    if winning_ticket[0] == ticket[0]:
        i += i
    else:
        i = 0
    return i

winning_ticket = [1,2,3,4,5,6]
ticket = [1,2,3,4,5,6]

print(winning_ticket)
print(ticket)
print (num_matches(winning_ticket, ticket))





