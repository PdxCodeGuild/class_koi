'''
PDX Code Guild - Class Koi
Lab 10 - ROT Cipher
Matt Walsh
'''


# Version 1
'''
# import ascii strings
from string import ascii_lowercase as lower, ascii_uppercase as upper

def encode(string):
    """
    Encodes input string with ROT13
    """
    # emptry string to build encoded string in
    new_string = ''
    # iterate through characters in string
    for char in string:
        # rotate and add to new_string if char is in lower/upper
        if char in lower:
            new_string += lower[lower.index(char) - 13]
        elif char in upper:
            new_string += upper[upper.index(char) - 13]
        # add original character if it was not a letter
        else:
            new_string += char
    # return reconstructed string
    return new_string

# ask user for string input and return results
input_string = input('Please enter a string to be encoded: ')
print(f'Your encoded string is:\n{encode(input_string)}')
'''


# Version 2

# import ascii strings
from string import ascii_lowercase as lower, ascii_uppercase as upper

def encode(string,rotations):
    """
    Encodes input string with ROT13
    """
    # emptry string to build encoded string in
    new_string = ''
    # iterate through characters in string
    for char in string:
        # rotate and add to new_string if char is in lower/upper
        if char in lower:
            new_string += lower[lower.index(char) - 26 + rotations]
        elif char in upper:
            new_string += upper[upper.index(char) - 26 + rotations]
        # add original character if it was not a letter
        else:
            new_string += char
    # return reconstructed string
    return new_string

# ask user for string input and number of rotations
input_string = input('Please enter a string to be encoded: ')
while True:
    rotations = input('Please enter the number of rotations: ')
    # convert to integer or prompt for re-entry
    try:
        rotations = int(rotations)
        break
    except:
        print('Enter rotations as an integer.')
# display results
print(f'Your encoded string is:\n{encode(input_string,rotations)}')