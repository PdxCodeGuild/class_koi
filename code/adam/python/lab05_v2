# Lab 05 - Blackjack Advice
# Version 2 - allow Aces to be worth 1 or 11

# create list of possible card choices
possible_cards = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
# create dictionary of card values
card_value = {
    'A1': 1,
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
    'A11': 11,
    0 : 0,
}

# show user list of possible card choices
print('\nPossible card inputs: A, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')

# ask user for first card
card_1 = input("\nWhat's your first card? ").upper()
# if user has Ace determine if they want to play it as 11 or 1
# create while loop to ensure correct Ace choice input
while card_1 == 'A':
    choice_1 = input('How would you like to play your Ace? (11 or 1): ').upper()
    if choice_1 == '11':
        card_1 = 'A11'
        break
    elif choice_1 == '1':
        card_1 = 'A1'
        break

card_2 = input("What's your second card? ").upper()
while card_2 == 'A':
    choice_2 = input('How would you like to play your Ace? (11 or 1): ' ).upper()
    if choice_2 == '11':
        card_2 = 'A11'
        break
    elif choice_2 == '1':
        card_2 = 'A1'
        break
card_3_option = input("Do you have a third card? (Y or N) ").upper()
if card_3_option == 'Y':
    card_3 = input("What's your third card? ").upper()
    while card_3 == 'A':
        choice_3 = input('How would you like to play your Ace? (11 or 1): ' ).upper()
        if choice_3 == '11':
            card_3 = 'A11'
            break
        elif choice_3 == '1':
            card_3 = 'A1'
            break
elif card_3_option == 'N':
    card_3 = 0
# calculate value of the blackjack hand
hand_value = card_value[card_1] + card_value[card_2] + card_value[card_3]
# if statements for the 3 possible outputs
if hand_value == 21:
    print(f'{hand_value} Blackjack!')
elif hand_value < 17:
    print(f'{hand_value} Hit')
elif hand_value < 21:
    print(f'{hand_value} Stay')
else:
    print(f'{hand_value} "Already Busted"')
