'''
Lab 5: Blackjack Advice
'''

cards_dict = {
    'Q': 10,
    'K': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 1,
}

while True:
    first_card = input("What's your first card? ").upper()
    if first_card in cards_dict:
        break
    else:
        print('not a valid card.')
    
while True:
    second_card = input("What's your second card? ").upper()
    if second_card in cards_dict:
        break
    else:
        print('not a valid card.')

while True:
    third_card = input("What's your third card? ").upper()
    if third_card in cards_dict:
        break
    else:
        print('not a valid card.')

player_points = cards_dict.get(first_card) + cards_dict.get(second_card) + cards_dict.get(third_card)

if player_points < 17:
    recommendation = 'hit'
elif player_points >= 17 and player_points < 21:
    recommendation = 'stay'
elif player_points == 21:
    recommendation = 'blackjack!'
elif player_points > 21:
    recommendation = 'busted'

print(player_points, recommendation, sep=' ')