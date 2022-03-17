# Guess the Number
# Version 2
# Mitch Chapman

import random

#random number generated here
NUMBER = random.randint(1, 10)

print ("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.")
print(f"You have unlimited attempts to guess the number.")

#game function defined here, runs until guess is the same as the random number above and records number of guesses
def game():
    try_count = 0
    while True:
        win = False
        global NUMBER
        
        while True:
            try:
                guess = int(input("\nMake a guess: "))
                break
            except ValueError:
                print("Please input a number only...")
                continue
        
        try_count += 1
        
        if NUMBER == guess:
            print(f"Congrats you win! 😃😃😃\nIt took you {try_count} guesses to get it right.")
            win = True
            break
        elif guess != NUMBER:
            print("Sorry, that's not it. Guess again.")  
                      
    if win is False:
        print(f"Sorry, you have run out of guesses.\nThe number was {NUMBER}.\nYou lose. 😭😭😭")


#game function runs here
game()
    
    
    