'''
ROT13 Cipher

Rotate by 13 alphabetical spaces.

Version 2: allow the user to input the amount of rotation.

Potential Improvement would be to fold the loops into functions that take variables
'''

user_cipher_ascii = ''
user_input = input('What is your message? ')

while True:
    try:
        cipher = int(input('Cipher key (rotation number): '))
        if cipher < 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('the cipher key must be an integer')

user_characters = [str(i) for i in user_input]

for i in range(len(user_characters)):
    if user_characters[i].isalpha():
        if user_characters[i].isupper() == True:
            user_cipher_ascii += chr((ord((user_characters[i])) - 65 + cipher) % 26 + 65)
        elif user_characters[i].islower() == True:
            user_cipher_ascii += chr((ord((user_characters[i])) - 97 + cipher) % 26 + 97)
    else:
        user_cipher_ascii += user_characters[i]

print(user_cipher_ascii)
