# Lab 03: Make Change
#-----------------------------------------------------------------------
# Version 1 - take input dollar amount and output number of coins
'''
# get dollar amount from user 
dollar_amount = input("Enter a dollar amount: ")
# change input string to float
dollar_amount = float(dollar_amount)
# multipy dollar_amount by 100 to get cents and change to int
cents_amount = int(dollar_amount * 100)
# first find out how many quarters are in dollar amount
quarters = cents_amount // 25
# cents left after quarter removal using modulus
cents_dimes = cents_amount % 25
# find out how many dimes
dimes = cents_dimes // 10
# cents left after dimes removal
cents_nickels = cents_dimes % 10
# find out how many nickels
nickels = cents_nickels // 5
# cents left after nickels removal which is pennies
cents_pennies = cents_nickels % 5
# find out how many pennies
pennies = cents_pennies

print(f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies')
'''
#---------------------------------------------------------------------------------
# Version 2 - store coin values in a list of tuples

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

