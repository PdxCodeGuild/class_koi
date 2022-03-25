##Version 1##
##Code##

# This generates advice based on the hand total.
def advice(x):
    int(x)
    if x <= 17:
        return("Hit!")
    elif (x > 17) and (x < 21):
        return("Stay")
    elif x == 21:
        return("Blackjack!!")
    elif x > 21:
        return("Already busted...")

# These are the card values, with no wild ace.

card_values = {
    "A":1, 
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
    "K":10,
    }

# This grabs inputs.

first = input("\nWhat is your first card?...")
second = input("What is your second card?...")
third = input("What is your third card?...")

# This tallies your hand value.

total = card_values[first] + card_values[second] + card_values[third]

# Output.

print(f"\n{total}  {advice(total)}\n")






