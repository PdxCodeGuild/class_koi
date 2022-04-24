# Lab 10: ROT Cipher
# Version 2
# Mitch Chapman


def translate_to_rot_13(input_str:str, encryption_or_decryption:str, offset:int):
    
    english_lowercase = "abcdefghijklmnopqrstuvwxyz"
    english_uppercase = english_lowercase.upper()
    english_full = english_lowercase + english_uppercase

    rot_13_lowercase_list = []

    for char in english_lowercase:
        char_index = ord(char) + offset
        if char_index > 122:
            char_index = 97 + (char_index - 123)
        if char_index < 97:
            char_index = 122 - (96 - char_index)

        rot_13_lowercase_list.append(chr(char_index))

    rot_13_lowercase = ''.join(rot_13_lowercase_list)
    rot_13_uppercase = rot_13_lowercase.upper()
    rot_13_full = rot_13_lowercase + rot_13_uppercase
    
    print(f"\n{'Encryption' if encryption_or_decryption == 'encrypt' else 'Decryption'} has been appplied to '{input_str}':")
    
    
    return(input_str.translate(input_str.maketrans(english_full, rot_13_full)))




print("\nThis is the 'ROT-13' encryption machine!")
while True:
    user_encryption_selection = input("Please indicate weather you would like to encrypt english to ROT-13 or from ROT-13 to english.\n(enter 'encrypt' or 'decrypt'): ").lower() or 'encrypt'
    if user_encryption_selection != "encrypt" and user_encryption_selection != "decrypt":
        print("This is an invalid selection. Try again.")
    else:
        break

user_offset_selection = int(input("Please indicate how many letters offset you would like (enter a negative or positive whole number): "))

user_input_phrase = input(f"Please enter a phrase you would like to have {'encrypted' if user_encryption_selection == 'encrypt' else 'decrypted'} by the ROT-13 encription machine:\n")
print(translate_to_rot_13(user_input_phrase, user_encryption_selection, user_offset_selection))











