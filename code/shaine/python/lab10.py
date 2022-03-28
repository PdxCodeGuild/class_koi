import string

#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 10: ROT Cipher 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

english = string.ascii_lowercase

# adds slice of second half of alphabet and joins in front of first half
rot_13  = english[13:] + english[:13]

'''split input string into a list'''
user_input = list(input('Enter word: '))

output = []

for i in range(0, len(user_input)):
    '''look up index of each letter using .index()'''
    index = english.index(user_input[i]) 
    '''use that index to find the matching ciphered letter'''
    output.append(rot_13[index])

'''output list as a string'''
print(''.join(output))
