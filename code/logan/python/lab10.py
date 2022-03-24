## Lab 10
## V 1.0
## Code


# variables used in encoding
standard_s = "abcdefghijklmnopqrstuvwxyz"
rot13_s = "nopqrstuvwxyzabcdefghijklm"

# function
def swap_rot13(string):
# encodes or decodes rot13
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

output = swap_rot13(message)
print(f"""
Your encoded/decoded message:
{output}
""")