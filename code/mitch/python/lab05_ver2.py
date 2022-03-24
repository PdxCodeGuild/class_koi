# Lab 5: Blackjack Advice
# Mitch Chapman

phrase = {
    "1": "first",
    "2": "second",
    "3": "third",
}

cards = {
    "A": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "J": 10, 
    "Q": 10, 
    "K": 10,
    "Large A": 11,
}

POINTS = 0
cards_in_hand = []

def calculate_score():
    global POINTS
    POINTS = 0
    for card in cards_in_hand:
        POINTS += cards[card]

print("This program will give you Blackjack advice, depending on your hand of 3 cards.")

#users cards are asked for and added to the cards_in_hand list. invalid inputs restarts loop.
while len(cards_in_hand) < 3:
    word = phrase[str(len(cards_in_hand) + 1)] 
    user_input = input(f"\nWhat is your {word} card? ('A','3','Q',etc.) ").upper()
    if user_input not in cards:
        print("Error: This is not a valid entry, please try again.\n")
    else:
        cards_in_hand.append(user_input)


#calculate score for first time
calculate_score()

#check if an Ace worth 1 point can be converted to an Ace worth 11 points, calculating score after conversion.
while POINTS <= 10:
    if "A" in cards_in_hand and POINTS <= 10:
        cards_in_hand[cards_in_hand.index("A")] = "Large A"

    calculate_score()

#results of the advice machine is given now
print("\n-|-|-|-|-|-|-|-|-|-|-|-  Below is your advice  -|-|-|-|-|-|-|-|-|-|-|-")

if POINTS > 21:
    print(f"{POINTS}... Sorry, already busted... 😭🤬😭")
elif POINTS == 21:
    print(f"{POINTS} Blackjack! 😃😎😃")
elif 17 <= POINTS < 21:
    print(f"{POINTS} Stay 🤨😅🤨")
else:
    print(f"{POINTS} Hit 😬🤔😬")















