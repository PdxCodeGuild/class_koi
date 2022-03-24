## Lab 10
## V 1.0
## Code


# variables used in encoding
standard_s = "abcdefghijklmnopqrstuvwxyz"
rot13_s = "nopqrstuvwxyzabcdefghijklm"

# function
def encode_rot13(string):
# takes in a string, returns that string in lowercase ROT13
    string_lower = string.lower()
    encoded_string = ""
    for char in string_lower:
        if char in standard_s:
            i = standard_s.index(char)
            encoded_string += rot13_s[i]
        else:
            encoded_string += char
    return encoded_string

# grabs user input

message = input("\nInput a message to be encrypted to ROT13:\n")

# output

output = encode_rot13(message)
print(f"""
Your message in ROT13:
{output}
""")