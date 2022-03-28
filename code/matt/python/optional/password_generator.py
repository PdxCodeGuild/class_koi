'''
PDX Code Guild - Class Koi
Optional Lab - Guess the Number
Matt Walsh
'''
 
# Version 1
''' 
# import random.choice 
from random import choice
from string import ascii_lowercase,  ascii_uppercase, digits, punctuation

# string holding all character options
char =  ascii_lowercase + ascii_uppercase + digits + punctuation

def generate(length):
    """
    Generate a password based on the length input as an int
    """
    # empty string variable for password
    password = ''
    # randomly select a character for each character in password length
    for x in range(length):
        password += choice(char)
    return password


# set password length
password_length = 16

# display results
print(f'Your password is: {generate(password_length)}')
'''


# Version 2
''' 
# import random.choice 
from random import choice
from string import ascii_lowercase,  ascii_uppercase, digits, punctuation

# string holding all character options
char =  ascii_lowercase + ascii_uppercase + digits + punctuation

def generate(length):
    """
    Generate a password based on the length input as an int
    """
    # empty string variable for password
    password = ''
    # randomly select a character for each character in password length
    for x in range(length):
        password += choice(char)
    return password


# set password length based on user input
while True:
    try:
        password_length = int(input('How long would you like your password to be? '))
        break
    except:
        print('Please enter your answer as a number.')

# display results
print(f'Your password is: {generate(password_length)}')
'''


# Version 3

# import random.choice 
from random import choice, shuffle
from string import ascii_lowercase,  ascii_uppercase, digits, punctuation

# string holding all character options
char =  {
    'lowercase':ascii_lowercase,
    'uppercase':ascii_uppercase,
    'digit':digits,
    'symbol':punctuation,
    }

def generate(length):
    """
    Generate a password based on the length input as a list
    """
    # empty list variable for password
    password = []
    # iterate through character types with counter
    i = 0
    for type in char:
        # add characters to password list based on user input
        for x in range(length[i]):
            password.append(choice(char[type]))
        # increment counter
        i += 1
    # shuffle and return password as string
    shuffle(password)
    return ''.join(password)

def display_choices(input):
    """
    Return user length choices as a multi-line string
    """
    # begin result string with total length
    result = f'\nYour password will be {sum(input)} long and contain:'
    # iterate through character types with counter
    i = 0
    for each in char:
        # add number and type to string (split between 2 lines for PEP 8)
        result += '\n' + str(input[i]) + ' '
        result += each + (' characters' if input[i] > 1 else ' character')
        # increment counter
        i += 1
    return result

# set password length based on user input
while True:
    # empty list to hold password length by character type
    password_length = []
    # ask for number of each type of character
    for each in char:
        # validate each entry
        while True:
            try:
                current_char = int(input(f'How many {each} characters would you like? '))
                password_length.append(current_char)
                break
            except:
                print('Please enter your answer as a number.')
    # display choices
    print(display_choices(password_length))
    # allow the user to confirm their choices
    while True:
        # variable to break outer loop
        break_loop = False
        confirm = input('Would you like to keep these settings? Y or N:')
        # if yes, set break_loop variable to True and break this loop
        if confirm.lower() == 'y':
            break_loop = True
            break
        # if no, break this loop to start at the top again
        elif confirm.lower() == 'n':
            break
        # if something else is entered, ask again
        else:
            print('I didn\'t understand that.')
    # if the user confirmed their choices, break the outer loop
    if break_loop == True:
        break

# display results
print(f'\nYour password is: {generate(password_length)}')