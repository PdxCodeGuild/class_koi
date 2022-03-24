# Lab 06 - Pick 6
# Program to pick 6 numbers check against winning numbers loop many times

# import random module
import random

# funtion to pick 6 random numbers from 1-99 without duplicates
def pick6():
    # create list of numbers 1-99
    nums = list(range(1,100))
    # use random shuffle module to shuffle list
    random.shuffle(nums)
    temp_ticket = nums[:6]
    return temp_ticket

# function to check winning ticket and purchased ticket
def num_matches(winning_ticket, ticket):
    matches_temp = 0
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matches_temp += 1
    return matches_temp

# define dictionary of winnings
# key is number of matches on ticket and value is amount won in dollars
winnings_dict = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000,
}
# Allow user to determine amount of pick 6 games
times_played = int(input('Enter the number of times you will play the Pick 6: '))

i = 0
cost = 0
winnings_sum = 0
while i < times_played:
    i += 1
    cost = cost -2
    winning_ticket = pick6() # winning_ticket = pick6(nums)
    ticket = pick6() # purchased ticket
    matches = num_matches(winning_ticket, ticket)
    winnings = winnings_dict[matches]
    winnings_sum += winnings
    balance = cost + winnings_sum
    
print(f'Total Lottery tickets purchased: {i}')
# print(f'Amount spent on lottery tickets: ${cost}')
# print(f'Sum of winnings: ${winnings_sum}')



# Version 2 Calculate ROI along with earnings and expenses
earnings = winnings_sum
expenses = cost
roi = (earnings - expenses) / expenses

print(f'ROI: {roi}%')
print(f'Earnings: ${earnings}')
print(f'Expenses: ${expenses}')
print(f'Net balance: ${balance}')