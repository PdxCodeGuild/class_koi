# Lab 10: ROT Cipher
# Version 1
# Mitch Chapman


english = "abcdefghijklmnopqrstuvwxyz"
rot_13 = "nopqrstuvwxyzabcdefghijklm"


def translate_to_rot_13(input_str:str):
    return(input_str.lower().translate(input_str.lower().maketrans(english, rot_13)))

print(translate_to_rot_13("abcd"))










########This is the code I am referencing. I wrote this for a codewars challange.##########

# def DNA_strand(dna):
#     return(dna.upper().translate(dna.upper().maketrans('ATGC', 'TACG')))   

# print(DNA_strand("aaa"))



#########More info here:
# https://www.w3schools.com/python/ref_string_maketrans.asp





