#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 5: Blackjack Advice 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# write a python program to give basic blackjack playing advice

# figure out the point value of each card individually

card_values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10,}

# ask the user for three playing cards

cards = ['first', 'second', 'third']

user_cards = 0

for card in cards:
    user_input = input(f"What's your {card} card? ")
    user_cards += card_values[user_input] 

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

if user_cards < 17:
    print(f'{user_cards} Hit')

elif user_cards >= 17 and user_cards < 21:
    print(f'{user_cards} Stay')

elif user_cards == 21:
    print(f'{user_cards} Blackjack!')

else:
    print(f'{user_cards} Already Busted')