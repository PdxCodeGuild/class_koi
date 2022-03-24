'''
PDX Code Guild - Class Koi
Optional Lab - Guess the Number
Matt Walsh
'''

from random import randint as rand
 
# Version 1
""" 
num = rand(1,10) # generate random number

i = 0 # counter for loop below

while i < 10: # allow 10 guesses
    while True: # loop for input validation, invalid entries will prompt for re-entry
        guess = input('Guess a number between 1 and 10! ') # prompt for user to guess
        try:
            guess = int(guess)
            if guess > 10 or guess < 1:
                print(f'{guess} is not a valid guess. Try again.')
            else:
                break
        except:
            print(f'{guess} is not a valid guess. Try again.')    
    if guess == num: # if guess is correct, display win message
        print(f'You win! {guess} is the right answer!')
        break
    else: # if guess is not correct, increment counter and prompt for another guess while informing user of number of guesses remaining
        i += 1
        print(f'{guess} is not the right answer. You have {10 - i} guesses left.')
"""

# Version 2
""" 
num = rand(1,100) # generate random number

i = 0 # counter for number of guesses

while True:
    while True: # loop for input validation, invalid entries will prompt for re-entry
        guess = input('Guess a number between 1 and 100, or type "done" to exit! ') # prompt for user to guess or exit
        try:
            guess = int(guess)
            if guess > 100 or guess < 1:
                print(f'{guess} is not a valid guess. Try again.')
            else:
                break
        except:
            if guess == 'done':
                break
            else:
                print(f'{guess} is not a valid guess. Try again.')    
    i += 1
    if guess == 'done':
        print('Goodbye.')
        break
    elif guess == num: # if guess is correct, display win message
        print(f'You win! {guess} is the right answer! It took you {i} guesses to figure it out.')
        break
    else: # if guess is not correct, prompt for another guess while informing user of number of guesses so far
        print(f'{guess} is not the right answer. You have guessed {i} times.')
"""

# Version 3
""" 
num = rand(1,100) # generate random number

i = 0 # counter for number of guesses

while True:
    while True: # loop for input validation, invalid entries will prompt for re-entry
        guess = input('Guess a number between 1 and 100, or type "done" to exit! ') # prompt for user to guess or exit
        try:
            guess = int(guess)
            if guess > 100 or guess < 1:
                print(f'{guess} is not a valid guess. Try again.')
            else:
                break
        except:
            if guess == 'done':
                break
            else:
                print(f'{guess} is not a valid guess. Try again.')    
    i += 1
    if guess == 'done':
        print('Goodbye.')
        break
    elif guess == num: # if guess is correct, display win message
        print(f'You win! {guess} is the right answer! It took you {i} guesses to figure it out.')
        break
    elif guess > num: # if guess is too high, inform user and prompt for another guess
        print(f'{guess} is too high. You have guessed {i} times.')
    else: # if guess is too low, inform user and prompt for another guess
        print(f'{guess} is too low. You have guessed {i} times.')
"""

# Version 4
""" 
num = rand(1,100) # generate random number

i = 0 # counter for number of guesses
last_guess = 0

while True:
    while True: # loop for input validation, invalid entries will prompt for re-entry
        guess = input('Guess a number between 1 and 100, or type "done" to exit! ') # prompt for user to guess or exit
        try:
            guess = int(guess)
            if guess > 100 or guess < 1:
                print(f'{guess} is not a valid guess. Try again.')
            else:
                break
        except:
            if guess == 'done':
                break
            else:
                print(f'{guess} is not a valid guess. Try again.')    
    i += 1
    if guess == 'done':
        print('Goodbye.')
        break
    elif guess == num: # if guess is correct, display win message
        print(f'You win! {guess} is the right answer! It took you {i} guesses to figure it out.')
        break
    elif guess > num and i > 1: # if guess is too high, inform user, let them know if it's closer/further than previous, and prompt for another guess
        print(f'{guess} is too high, {"but closer than" if abs(num - guess) < abs(num - last_guess) else "and further than" if abs(num - guess) > abs(num - last_guess) else "and the same distance away as"} your last guess. You have guessed {i} times.')
    elif guess < num and i > 1: # if guess is too low, inform user, let them know if it's closer/further than previous, and prompt for another guess
        print(f'{guess} is too low, {"but closer than" if abs(num - guess) < abs(num - last_guess) else "and further than" if abs(num - guess) > abs(num - last_guess) else "and the same distance away as"} your last guess. You have guessed {i} times.')
    elif guess > num: # if first guess is too high, inform user and prompt for another guess
        print(f'{guess} is too high. You have guessed {i} times.')
    else: # if first guess is too low, inform user and prompt for another guess
        print(f'{guess} is too low. You have guessed {i} times.')
    last_guess = guess # store current guess for evaluation against next guess
"""

# Version 5

while True: # input validation to check if user entry is an integer and is within raneg
    num = input('Enter a number between 1 and 100, and I will guess what it is: ')
    try:
        num = int(num)
        if num < 1 or num > 100:
            print(f'{num} is not a valid entry. Try again.')
        else:
            break
    except:
        print(f'{num} is not a number. Try again.')

guess_list = [] # empty list to store guesses
i = 0 # variable to store number of guesses

while True:
    guess = rand(1,100) # make a random guess
    i += 1 # increment guess counter
    if guess == num: # if guess is correct, report that with number of guesses and list of previous guesses
        print(f'I guessed it in {i} {"tries" if i > 1 else "try"}. Before I got it right I guessed all these numbers: \n{", ".join(guess_list)}')
        break
    else:
        guess_list.append(str(guess)) # add incorrect guess to list