# Version 1
cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}
score = 0

first_card = input('What is your first card? ')
score = cards[first_card]

second_card = input('What is your second card? ')
score += cards[second_card]

third_card = input('What is your third card? ')
score += cards[third_card]

if score < 17:
    print(f'{score} Hit')

elif score > 17 and score > 21:
    print(f'{score} Stay')

if score == 21:
    print(f'{score} Blackjack!')

if score > 21:
    print(f'{score} Bust!')