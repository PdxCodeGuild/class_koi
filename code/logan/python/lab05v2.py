# This generates advice in all circumstances but the triple A scenario.
def advice(x):
    int(x)
    if x < 17:
        return("Hit!")
    elif (x > 17) and (x < 21):
        return("Stay")
    elif x == 21:
        return("Blackjack!!")
    elif x > 21:
        return("Already busted...")

ace_counter = 0

# The ace value never actually comes into play.
card_values = {
    "A": [1,11], 
    "2":2, 
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":11,
    }

player_cards = []
player_cards_sorted = []

first = input("\nWhat is your first card?...")
second = input("What is your second card?...")
third = input("What is your third card?...")

player_cards.append(first)
player_cards.append(second)
player_cards.append(third)

for x in player_cards:
    if x == "A":
        ace_counter += 1

# This all just remakes the player card list with the aces loaded in front.  I'm sure there's a better way to do this... 

if ace_counter == 1:
        player_cards_sorted.append("A")
        player_cards.remove("A")
elif ace_counter == 2:
    player_cards_sorted.append("A")
    player_cards_sorted.append("A")
    player_cards.remove("A")
    player_cards.remove("A")
elif ace_counter == 3:
    player_cards_sorted.append("A")
    player_cards_sorted.append("A")
    player_cards_sorted.append("A")
    player_cards.remove("A")
    player_cards.remove("A")
    player_cards.remove("A")

for x in player_cards:
    player_cards_sorted.append(x)

if ace_counter == 0:
    total_noA = (card_values[player_cards_sorted[0]] + card_values[player_cards_sorted[1]] + card_values[player_cards_sorted[2]])
    print(f"\n{total_noA} {advice(total_noA)}\n")

if ace_counter == 1:
    total1 = 1 + card_values[player_cards_sorted[1]] + card_values[player_cards_sorted[2]]
    total2 = 11 + card_values[player_cards_sorted[1]] + card_values[player_cards_sorted[2]]
    print("\nLive possibilities...")
    print(f"{total1} {advice(total1)}")
    if total2 <= 21:
        print(f"{total2} {advice(total2)}")

if ace_counter == 2:
    total1 = 1 + 1 + card_values[player_cards_sorted[2]]
    total2 = 11 + 1 + card_values[player_cards_sorted[2]]
    # total3 = 11 + 11  + card_values[player_cards_sorted[2]]
    print("\nLive possibilities...")
    print(f"{total1} {advice(total1)}")
    if total2 <= 21:
        print(f"{total2} {advice(total2)}")
    # I just realized this elif will never be triggered, so I commented it and line 83 out.
    # elif total3 <= 21:
    #     print(f"{total3} {advice(total3)}")

if ace_counter == 3:
    print("\nLive possibilities...")
    print("3  Hit!")
    print("13  Hit!\n")