'''
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
'''

# encrypt rot13
def rot13(input):
    # ascii values a - z = 97 - 122
    rotted = []
    input = input.lower()
    # convert letter to ascii value, add 13, and convert back to letter
    for letter in input:
        # check if letter is a letter
        if(not(letter.isalpha())):
            rotted.append(letter)
            continue
        # if value reaches passed 'z' (122) go back to 'a' (97)
        letter = ord(letter)
        letter += 13
        
        if(letter > 122):
            letter -= 122
            letter += 97
        letter = chr(letter)
        rotted.append(letter)

    rotted = ''.join(rotted)

    return rotted


# decrypt rot13
def unrot13(input):
    unrotted = []
    input = input.lower()
    # convert each letter to ascii value, minus 13, and convert back to letter
    for letter in input:
        # check if letter is a letter
        if(not(letter.isalpha())):
            unrotted.append(letter)
            continue
        letter = ord(letter)
        letter -= 13
        
        # if value reaches below 'a' (97) go back to 'z' (122)
        if(letter < 97):
            letter += 122
            letter -= 97
        letter = chr(letter)
        unrotted.append(letter)

    unrotted = ''.join(unrotted)

    return unrotted

user_input = input("What do you want to encrypt? ")
print(f"This is your encrypted input:\n{rot13(user_input)}")

user_decrypt = input("What do you want to decrypt? ")
print(f"This is your decrypted output:\n{unrot13(user_decrypt)}")
# print(unrot13("huvg vg n hrgh")) # this is a test

# ------------- version two ---------------- #

# Allow the user to input the amount of rotation used in the encryption / decryption.
def version_two_rotted(input, rotation):
    count = 0

    while(count <= rotation):
        input = rot13(input)
        count += 1

    return input


def version_two_unrotted(input, rotation):
    count = 0

    while(count <= rotation):
        input = unrot13(input)
        count += 1

    return input

user_input = input("What do you want to encrypt? ")
user_encrypt_count = input("How many times do you want to run encryption? ")
print(f"This is your encrypted input:\n{version_two_rotted(user_input, int(user_encrypt_count))}")

user_decrypt = input("What do you want to decrypt? ")
user_decrypt_count = input("How many times do you need to run decryption? ")
print(f"This is your decrypted output:\n{version_two_unrotted(user_decrypt, int(user_decrypt_count))}")
