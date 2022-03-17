# Lab 05 - Blackjack Advice
# Version 1

print('Possible card inputs: A, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')
card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

card_value = {
    'A': 1,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

hand_value = card_value[card_1] + card_value[card_2] + card_value[card_3]

print(hand_value)