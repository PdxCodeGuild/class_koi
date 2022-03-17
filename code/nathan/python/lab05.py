'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
'''

def cardConversion(card):
    if(card == 'A'):
        return 1
    
    elif(card == 'J' or card == 'Q' or card == 'K'):
        return 10
    
    return int(card)

def versionOne():

    result = 0

    firstCard = input("What's your first card? ").upper()
    secondCard = input("What's your second card? ").upper()
    thirdCard = input("What's your second card? ").upper()

    firstCard = cardConversion(firstCard)
    secondCard = cardConversion(secondCard)
    thirdCard = cardConversion(thirdCard)

    result = firstCard + secondCard + thirdCard

    if(result < 17):
        print(f"{result} Hit")
    elif(result >= 17 and result < 21):
        print(f"{result} Stay")
    elif(result == 21):
        print(f"Blackjack!")
    elif(result > 21):
        print(f"Already Busted")

versionOne()