'''
PDX Code Guild - Class Koi
Lab 03 - Make Change
Matt Walsh
'''


# Version 1
""" 
coins = [] # empty list for number of coins to be added to
coin_types = [('quarter', 'quarters'), ('dime', 'dimes'), ('nickel', 'nickels'), ('penny', 'pennies')] # coin types in tuples with singular and plural forms

while True: # input validation loop
    pocket = input('How much money\'s in your pocket? ').lstrip("$") # request input and strip dollar sign if present
    try: # attempt to convert input to a float
        pocket = float(pocket)
        break
    except: # if conversion to float fails, display an error message and prompt for re-entry
        print('Please enter your answer as a number (e.g. "1.23" or "$1.23")')

# use floor division to find number of each coin, append to list, and use rounded modulus to determine what is left uncounted while avoiding floating point errors
coins.append(int(pocket // .25))
pocket = round(pocket % .25, 2)
coins.append(int(pocket // .1))
pocket = round(pocket % .1, 2)
coins.append(int(pocket // .05))
pocket = round(pocket % .05, 2)
coins.append(int(round(pocket / .01)))

i = 0 # counter int for loop below

for coin in coins: # loop through coins list converting ints to strings and adding coin denomination in singular or plural form to each
    if coin == 1: 
        coins[i] = str(coin) + ' ' + coin_types[i][0]
    elif coin > 1:
        coins[i] = str(coin) + ' ' + coin_types[i][1]
    i += 1

coins = [coin for coin in coins if coin != 0] # loop through coins keeping only non-zero values

coins[-1] = "and " + coins[-1] # add "and" to last coin

print(f'You have {", ".join(coins) if len(coins) > 2 else " ".join(coins)} in your pocket.') # join list and print results only including a comma if there are more than 2 types of coins listed
"""

# Version 2

coins = [] # empty list for number of coins to be added to
coin_types = [ # list of tuples with coin names and values
    (.5, 'half-dollar', 'half-dollars'),
    (.25, 'quarter', 'quarters'),
    (.1, 'dime', 'dimes'),
    (.05, 'nickel', 'nickels'),
    (.01, 'penny', 'pennies')
]

while True: # input validation loop
    pocket = input('How much money\'s in your pocket? ').lstrip("$") # request input and strip dollar sign if present
    try: # attempt to convert input to a float
        pocket = float(pocket)
        break
    except: # if conversion to float fails, display an error message and prompt for re-entry
        print('Please enter your answer as a number (e.g. "1.23" or "$1.23")')

i = 0 # counter int for loop below

for type in coin_types: # loop through each type of coin
    x = int(pocket // type[0]) # use floor division to find number of each coin
    pocket = round(pocket % type[0], 2) # use rounded modulus to determine what is left uncounted while avoiding floating point errors
    if x == 1: # append to coins list as strins with the singular coin name if there is only 1 coin
        coins.append(str(x) + ' ' + str(coin_types[i][1]))
    elif x > 1: # append to coins list as strins with the plural coin name if there are more than 1 coins
        coins.append(str(x) + ' ' + str(coin_types[i][2]))
    i += 1

coins[-1] = "and " + coins[-1] # add "and" to last coin

print(f'You have {", ".join(coins) if len(coins) > 2 else " ".join(coins)} in your pocket.') # join list and print results only including a comma if there are more than 2 types of coins listed