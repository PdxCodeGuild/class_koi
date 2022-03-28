# Version 1
#basic dictionary with card face and point value
cards = { "A" : 1, "K" : 10, "Q": 10,"J": 10,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10}

card_1 = input("What is a card 1 in your hand? ")
card_2 = input("What is a card 2 in your hand? ")
card_3 = input("What is a card 3 in your hand? ")

#adding point values to calculate players hand score
players_hand = cards[card_1] + cards[card_2] + cards[card_3]
print (players_hand)

if players_hand <= 17:
    print ("Hit")
elif players_hand >= 17 and players_hand <= 21:
        print ("Stay")
elif players_hand == 21:
        print ("Blackjack!")
elif players_hand > 21:
        print("You Busted")
