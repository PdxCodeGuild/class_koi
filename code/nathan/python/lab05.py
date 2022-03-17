'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
'''

def versionOne():

    def cardConversion(card):
        if(card == 'A'):
            return 1
    
        elif(card == 'J' or card == 'Q' or card == 'K'):
            return 10
    
        return int(card)

    result = 0

    firstCard = input("What's your first card? ").upper()
    secondCard = input("What's your second card? ").upper()
    thirdCard = input("What's your third card? ").upper()

    firstCard = cardConversion(firstCard)
    secondCard = cardConversion(secondCard)
    thirdCard = cardConversion(thirdCard)

    result = firstCard + secondCard + thirdCard

    if(result < 17):
        print(f"{result} Hit")
    elif(result >= 17 and result < 21):
        print(f"{result} Stay")
    elif(result == 21):
        print(f"{result} Blackjack!")
    elif(result > 21):
        print(f"{result} Already Busted")

def versionTwo():

    def cardConversion(card):
        if(card == 'A'):
            return 11
    
        elif(card == 'J' or card == 'Q' or card == 'K'):
            return 10
    
        return int(card)

    cardList = []
    
    result = 0

    firstCard = input("What's your first card? ").upper()
    secondCard = input("What's your second card? ").upper()
    thirdCard = input("What's your third card? ").upper()

    cardList.append(cardConversion(firstCard))
    cardList.append(cardConversion(secondCard))
    cardList.append(cardConversion(thirdCard))

    result = sum(cardList) # Store user's cards into a list

    # If the user's hand has aces and has a bust, convert aces to value of 1
    if(11 in cardList and result > 21):
        count = 0

        # The user may have multiple aces which could cause a bust
        while(result > 21 or count < len(cardList)):
            if(cardList[count] == 11):
                cardList[count] = 1
                result = sum(cardList)

            count += 1

    if(result < 17):
        print(f"{result} Hit")
    elif(result >= 17 and result < 21):
        print(f"{result} Stay")
    elif(result == 21):
        print(f"{result} Blackjack!")
    elif(result > 21):
        print(f"{result} Already Busted")

# versionOne()
versionTwo()