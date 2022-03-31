# lab 05 version 1 ---- #

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
# user_list = []

card1 = input('Enter your first card: ')
card2 = input('Enter your second card: ')
card3 = input('Enter your third card: ')
# user_list.append(card1)
# user_list.append(card2)
# user_list.append(card3)
# print(user_list) 

# changing value of each user's card to an integer in order to add
value1 = int(cards[card1])
value2 = int(cards[card2])
value3 = int(cards[card3])

# adding together each value of user's cards
total = value1 + value2 + value3
print(total) # total value of user's cards


if total < 17:
    print(f'{total} hit!')
elif total >= 17 and total < 21:
    print(f'{total} stay!')
elif total == 21:
    print(f'{total} Blackjack!')
else:
    print('Already busted!')
