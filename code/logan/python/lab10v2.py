# Lab 10 V2, finished
##Code

standard_s = "abcdefghijklmnopqrstuvwxyz"

message = input("\nInput a message to be encrypted or decrypted:\n")
try:
    rotations = input("\nInput a number of rotations:\n")
    rotations = int(rotations)
except:
    print("Invalid input.  Please input a number.\n")

while True:
    process = input("\nEnter E to encrypt or D to decrypt:\n")
    process = process.upper()
    if (process != "E") and (process != "D"):
        print("Invalid input\n")
    else:
        break

def encryptor(string, number):
    string_lower = string.lower()
    encoded_string = ""
    for char in string_lower:
        if char in standard_s:
            i = standard_s.index(char)
            imod = i + number
            while imod > 25:
                imod -= 26
        encoded_string += standard_s[imod]
    return encoded_string

def decryptor(string, number):
    string_lower = string.lower()
    encoded_string = "" 
    for char in string_lower:
        if char in standard_s:
            i = standard_s.index(char)
            imod = i - number
            while imod < 0:
                imod += 26
        encoded_string += standard_s[imod]
    return encoded_string

if process == "E":
    print(f"""
Your message after {rotations} rotations:
{encryptor(message, rotations)}
""")
else:
    print(f"""
Your message after {rotations} rotations:
{decryptor(message, rotations)}
""")