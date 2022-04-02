'''
PDX Code Guild - Class Koi
Optional Lab - Rock Paper Scissors
Matt Walsh
'''

 
# Version 1
'''
# import choice for computer selection
from random import choice

# dictionary of choices with dictionaries of win/lose/tie choices
choices = {
    'Rock':{
        'Rock':'It\'s a tie.',
        'Paper':'You lose.',
        'Scissors':'You win!',
    },
    'Paper':{
        'Rock':'You win!',
        'Paper':'It\'s a tie.',
        'Scissors':'You lose.',
    },
    'Scissors':{
        'Rock':'You lose.',
        'Paper':'You win!',
        'Scissors':'It\'s a tie.',
    },
}

def rps(user):
    """
    Compares user input to random computer selection to determine winner
    """
    # computer selects choice from keys
    computer = choice(list(choices.keys()))
    # return win/lose/tie from dictionary
    return choices[user][computer], computer

while True:
    # ask for user input and validate against choices dict
    user_choice = input('Choose Rock, Paper, or Scissors: ').title()
    if user_choice in choices:
        break

# store and display result of function call
result = rps(user_choice)
print(f'You chose {user_choice}, I chose {result[1]}. {result[0]}')
'''

 
# Version 2

# import choice for computer selection
from random import choice

# dictionary of choices with dictionaries of win/lose/tie choices
choices = {
    'Rock':{
        'Rock':'It\'s a tie.',
        'Paper':'You lose.',
        'Scissors':'You win!',
    },
    'Paper':{
        'Rock':'You win!',
        'Paper':'It\'s a tie.',
        'Scissors':'You lose.',
    },
    'Scissors':{
        'Rock':'You lose.',
        'Paper':'You win!',
        'Scissors':'It\'s a tie.',
    },
}

def rps(user):
    """
    Compares user input to random computer selection to determine winner
    """
    # computer selects choice from keys
    computer = choice(list(choices.keys()))
    # return win/lose/tie from dictionary
    return choices[user][computer], computer

# list to hold scores [user,computer]
scores = [0,0]

while True:
    # continue playing until user quits
    while True:
        # ask for user input and validate against choices dict
        user_choice = input('Choose Rock, Paper, or Scissors: ').title()
        if user_choice in choices:
            break
        else:
            print('That\'s not a valid choice. Try again.')
    # store and display result of function call
    result = rps(user_choice)
    print(f'You chose {user_choice}, I chose {result[1]}. {result[0]}')
    # update and display score and who's winning
    if result[0] == 'You win!':
        scores[0] += 1
    elif result[0] == 'You lose.':
        scores[1] += 1
    if scores[0] > scores[1]:
        win_lose = 'your lead'
    elif scores[0] < scores[1]:
        win_lose = 'my lead'
    else:
        win_lose = 'we\'re tied'
    print(f'The current score is {scores[0]}-{scores[1]}, {win_lose}.')
    while True:
        # set variable to break out of nested loop
        break_out = False
        # ask user if they want to play again, validate, break out if chosen
        what_next = input('Would you like to play again? Y or N? ')
        if what_next.lower() == 'n':
            # set break_out to True to break out of nested loop
            break_out = True
            break
        elif what_next.lower() == 'y':
            break
        else:
            # prompt to try again if not "y" or "n"
            print('I didn\'t understand that.')
    # break if user chose to quit
    if break_out == True:
        break