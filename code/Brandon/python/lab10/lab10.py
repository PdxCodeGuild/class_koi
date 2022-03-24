# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Version 1
alphachar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '', '!']
rot13char = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', ' ', '', '!']

user_char = input('Please input the string you would like to convert rot13: ')

outputrot = ''
outputalpha = ''
user_char = user_char.lower()

while user_char.isnumeric():
    user_char = input('Please input the string you would like to convert rot13, NO NUMBERS!: ')
else:
    pass

# converts alphachar index to rot13 index
for a in user_char:
    index = []
    index = alphachar.index(a)
    rot13 = rot13char.index(a)
    rot13 = rot13char[index]
    outputrot += rot13
    outputalpha += a

print(f'User input: {outputalpha} \nRot13 output: {outputrot}')
