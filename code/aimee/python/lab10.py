# Lab 10, ROT13 ---- #

english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

user_input = input('Enter a string of characters to be encrypted: ')

def encrypt(user_input):
    '''Encodes input with ROT13'''
    user_input.split() # turn user input to list 
    output = [] # output list; will convert to string later
    for letter in user_input:
        if letter == 'a':
            output.append(rot13[0])
        if letter == 'b':
            output.append(rot13[1])
        if letter == 'c':
            output.append(rot13[2])
        if letter == 'd':
            output.append(rot13[3])
        if letter == 'e':
            output.append(rot13[4])
        if letter == 'f':
            output.append(rot13[5])
        if letter == 'g':
            output.append(rot13[6])
        if letter == 'h':
            output.append(rot13[7])
        if letter == 'i':
            output.append(rot13[8])
        if letter == 'j':
            output.append(rot13[9])
        if letter == 'k':
            output.append(rot13[10])
        if letter == 'l':
            output.append(rot13[11])
        if letter == 'm':
            output.append(rot13[12])
        if letter == 'n':
            output.append(rot13[13])
        if letter == 'o':
            output.append(rot13[14])
        if letter == 'p':
            output.append(rot13[15])
        if letter == 'q':
            output.append(rot13[16])
        if letter == 'r':
            output.append(rot13[17])
        if letter == 's':
            output.append(rot13[18])
        if letter == 't':
            output.append(rot13[19])
        if letter == 'u':
            output.append(rot13[20])
        if letter == 'v':
            output.append(rot13[21])
        if letter == 'w':
            output.append(rot13[22])
        if letter == 'x':
            output.append(rot13[23])
        if letter == 'y':
            output.append(rot13[24])
        if letter == 'z':
            output.append(rot13[25])
                
    output_string = '' # converting each list item to string
    for x in output:
        output_string += '' + x # output_string = output_string + '' + x
    return output_string

output_string = encrypt(user_input)

def decrypt(output_string):
    '''Decodes ROT13 encryption to standard English'''
    output_string.split() # turn user input to list 
    output_2 = [] # output list; will convert to string later
    for letter in output_string:
        if letter == 'n':
            output_2.append(english[0])
        if letter == 'o':
            output_2.append(english[1])
        if letter == 'p':
            output_2.append(english[2])
        if letter == 'q':
            output_2.append(english[3])
        if letter == 'r':
            output_2.append(english[4])
        if letter == 's':
            output_2.append(english[5])
        if letter == 't':
            output_2.append(english[6])
        if letter == 'u':
            output_2.append(english[7])
        if letter == 'v':
            output_2.append(english[8])
        if letter == 'w':
            output_2.append(english[9])
        if letter == 'x':
            output_2.append(english[10])
        if letter == 'y':
            output_2.append(english[11])
        if letter == 'z':
            output_2.append(english[12])
        if letter == 'a':
            output_2.append(english[13])
        if letter == 'b':
            output_2.append(english[14])
        if letter == 'c':
            output_2.append(english[15])
        if letter == 'd':
            output_2.append(english[16])
        if letter == 'e':
            output_2.append(english[17])
        if letter == 'f':
            output_2.append(english[18])
        if letter == 'g':
            output_2.append(english[19])
        if letter == 'h':
            output_2.append(english[20])
        if letter == 'i':
            output_2.append(english[21])
        if letter == 'j':
            output_2.append(english[22])
        if letter == 'k':
            output_2.append(english[23])
        if letter == 'l':
            output_2.append(english[24])
        if letter == 'm':
            output_2.append(english[25])
                
    decrypt_string = '' # converting each list item to string
    for x in output_2:
        decrypt_string += '' + x # output_string = output_string + '' + x
    return decrypt_string


while True:
    if user_input.isalpha():
        print(f'Your encrypted string is: {encrypt(user_input)}')
        print(f'Your decrypted string is: {decrypt(output_string)}')
        break
    else:
        print('Please only use letters.')
        break
