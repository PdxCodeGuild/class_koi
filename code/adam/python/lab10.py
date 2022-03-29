# Lab 10 - ROT Cipher
# Version 1

# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the -
# - same as decryption.

# create string variable of lower case alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# function to encrpyt
def rot_cipher(string_message):
    # create variable of empty string to hold encrypted message
    encrypted_message = ""
    # 'for loop' to iterate thru message and encrypt or decrypt
    for character in input_message:
        if character.isalpha():
            encrypted_message += alphabet[(alphabet.index(character) + rot_amount) % 26]
        else:
            encrypted_message += character
    return encrypted_message

#--------------------------------------------------------------------------------------
# Version 2 - allow user to define amount of rotation of cipher

# function to decrpyt
def rot_decipher(string_message):
    # create variable of empty string to hold encrypted message
    decrypted_message = ""
    # 'for loop' to iterate thru message and encrypt or decrypt
    for character in input_message:
        if character.isalpha():
            decrypted_message += alphabet[(alphabet.index(character) - rot_amount) % 26]
        else:
            decrypted_message += character
    return decrypted_message


decision = input('\nEnter (1) to encrypt or Enter (2) to decrypt message: ')
if decision == '1':
    rot_amount = int(input('Enter amount of rotatation: '))
    input_message = input('Enter message to be encrypted: ')
    input_message = input_message.lower()
    output_message = rot_cipher(input_message)
    print(f'Encrypted message with rotation of {rot_amount}: {output_message}')
elif decision == '2':
    rot_amount = int(input('Enter amount of rotation: '))
    input_message = input('Enter the message to be decrypted: ')
    input_message = input_message.lower()
    output_message = rot_decipher(input_message)
    print(f'Decrypted message with rotation of {rot_amount}: {output_message}')
else:
    print('Invalid choice')
   