# Guess the Number
# Version 1
# Mitch Chapman

import random

#random number generated here and number of guesses for game can be adjusted here
NUMBER = random.randint(1, 10)
num_of_guesses = 10

print ("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.")


#game function defined here, runs until tries runs out or guess is the same as the random number above
def game(tries):
    while tries > 0:
        win = False
        global NUMBER
        
        print(f"\nYou have {tries} attempts remaining to guess the number.")
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except ValueError:
                print("Please input a number only...")
                continue
        
        if NUMBER == guess:
            print("Congrats you win! 😃😃😃")
            win = True
            break
        elif guess != NUMBER:
            tries -= 1
            if tries > 0:
                print("Sorry, that's not it. Guess again.")  
                      
    if win is False:
        print(f"Sorry, you have run out of guesses.\nThe number was {NUMBER}.\nYou lose. 😭😭😭")


#game function runs here, with number of guesses from above as an input
game(num_of_guesses)
    
    
    