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
}

cards_in_hand = []
points = 0

print("This program will give you Blackjack advice, depending on your hand of 3 cards.")

while len(cards_in_hand) < 3:
    word = phrase[str(len(cards_in_hand) + 1)] 
    user_input = input(f"\nWhat is your {word} card? ('A','3','Q',etc.) ").upper()
    if user_input not in cards:
        print("Error: This is not a valid entry, please try again.\n")
    else:
        cards_in_hand.append(user_input)

for card in cards_in_hand:
    points += cards[card]

if points > 21:
    print(f"{points}... Sorry, already busted... 😭🤬😭")
elif points == 21:
    print(f"{points} Blackjack! 😃😎😃")
elif 17 <= points < 21:
    print(f"{points} Stay 🤨😅🤨")
else:
    print(f"{points} Hit 😬🤔😬")















