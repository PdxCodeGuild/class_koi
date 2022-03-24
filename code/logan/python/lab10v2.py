# Work in progress

standard_s = "abcdefghijklmnopqrstuvwxyz"

message = input("\nInput a message to be encrypted to ROT13:\n")
roations = input("\nInput a number of rotations:\n")

def encryptor(string, number):
    string_lower = string.lower()
    encoded_string = ""
    for char in string_lower:
        if char in standard_s:
            i = standard_s.index(char)
            imod = i + number
            while imod > 25:
                imod -= 26
        
