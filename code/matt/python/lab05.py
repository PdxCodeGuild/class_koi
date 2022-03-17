'''
PDX Code Guild - Class Koi
Lab 05 - Blackjack Advice
Matt Walsh
'''

 
# Version 1
""" 
# dictionary of cards and their point values
cards = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
}

# dictionary to prompt for each card in english
card_in_hand = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth',
    'thirteeth',
    'fourteenth',
]

while True: # input validation for number of cards in player's hand, which can't exceed 14
    number_of_cards = input('Please tell me how many cards are in your hand: ')
    try:
        number_of_cards = int(number_of_cards)
        if number_of_cards < 1 or number_of_cards > 14:
            print('I\'m sorry, that\'s not a valid hand size. Try again.')
        else:
            break
    except:
        print('That doesn\'t sound right. Try again.')

hand_value = 0 # integer to subtotal value of player's hand

for x in range(number_of_cards): # loop through each card in the player's hand and ask what it is
    while True:
        card_value = input(f'Please tell me what your {card_in_hand[x]} card is: ').upper()
        if card_value not in cards: # validate input against dictionary
            print('I didn\'t recognize that. Please enter the card as a single character (i.e. A, 4, J, or K).')
        else: # if card is valid, add to hand value subtotal and exit loop
            hand_value += cards[card_value]
            break

print(f'Your hand is worth {hand_value} points.', end=' ') # show hand value

# determine status of player's hand and advise
if hand_value < 17:
    print('You should hit.')
elif hand_value == 21:
    print('Blackjack!')
elif hand_value > 21:
    print('You already busted.')
else:
    print('You should stay.')
"""

# Version 2

# dictionary of cards and their point values
cards = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
}

# dictionary to prompt for each card in english
card_in_hand = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth',
    'thirteeth',
    'fourteenth',
]

while True: # input validation for number of cards in player's hand, which can't exceed 14
    number_of_cards = input('Please tell me how many cards are in your hand: ')
    try:
        number_of_cards = int(number_of_cards)
        if number_of_cards < 1 or number_of_cards > 14:
            print('I\'m sorry, that\'s not a valid hand size. Try again.')
        else:
            break
    except:
        print('That doesn\'t sound right. Try again.')

player_hand = [] # empty list to hold player's hand

for x in range(number_of_cards): # loop through each card in the player's hand and ask what it is
    while True:
        card_value = input(f'Please tell me what your {card_in_hand[x]} card is: ').upper()
        if card_value not in cards: # validate input against dictionary
            print('I didn\'t recognize that. Please enter the card as a single character (i.e. A, 4, J, or K).')
        else: # if card is valid, add to hand list and exit loop
            player_hand.append(card_value)
            break

def special_sort(x): # function to return point value of card for use in hand sorting
    return cards[x]

player_hand.sort(reverse=True, key=special_sort) # sort player hand so aces are last

hand_value = 0 # integer to subtotal value of player's hand

# add value of each card in hand to subtotal except for the last card
for card in player_hand[:-1]:
    hand_value += cards[card]

# add value of last card in hand to subtotal
if player_hand[-1] != 'A': # if it isn't an ace, add like normal
    hand_value += cards[player_hand[-1]]
elif hand_value + 11 > 21: # if it is an ace and adding 11 would bust, add 1 instead
    hand_value += cards[player_hand[-1]]
else: # if adding 11 won't bust, add 11
    hand_value += 11

print(f'Your hand is worth {hand_value} points.', end=' ') # show hand value

# determine status of player's hand and advise
if hand_value < 17:
    print('You should hit.')
elif hand_value == 21:
    print('Blackjack!')
elif hand_value > 21:
    print('You already busted.')
else:
    print('You should stay.')