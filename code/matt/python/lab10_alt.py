'''
PDX Code Guild - Class Koi
Lab 10 - ROT Cipher (alternate)
Matt Walsh
'''


# Version 1
'''
from string import ascii_lowercase as letters

def encode(s):
    """
    Encodes input string with ROT13
    """
    # generate cipher
    cipher = ''.join([letters[i-13] for i,char in enumerate(letters)])
    # return encoded message
    return ''.join([cipher[i] for i,char in enumerate(s)])

# prompt for input and display encoded message
print(encode(input('Please enter a string to encode with ROT13: ')))
'''


# Version 2

# import alphabet string
from string import ascii_lowercase as letters
# import custom module - run from class_koi - if issues, comment next 3 lines out & toggle commenting on lines 50 & 51#########################################
import sys
sys.path.append('./code/matt/python/modules') # run from class_koi
from input_validation import valid_int, valid_str

def encode_decode(s,n,m):
    """
    Encodes input string with ROT13
    """
    # generate cipher
    cipher = ''.join([letters[i-26+n] for i,char in enumerate(letters)])
    # return decoded message
    if m == 'd':
        return ''.join([cipher[i-n] for i,char in enumerate(s)])
    # return encoded message
    return ''.join([cipher[i] for i,char in enumerate(s)])

# prompt for input and display encoded message
m = valid_str('Please choose a mode (e for encode, d for decode): ',['e','d'],None,False)
n = valid_int('Please enter the number of rotations to use in encoding: ',None,1,26)
s = input(f'Please enter a string to encode with ROT{n}: ')
# n = int(input('Please enter the number of rotations to use in encoding: ')) # uncomment if import issues with input_validation module
print(encode_decode(s,n,m))