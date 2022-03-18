# lab 04 version 1 ---- #

# ones = {
#     0:'zero',
#     1:'one',
#     2:'two',
#     3:'three',
#     4:'four',
#     5:'five',
#     6:'six',
#     7:'seven',
#     8:'eight',
#     9:'nine',
# }

# teens = {
#     10:'ten',
#     11:'eleven',
#     12:'twelve',
#     13:'thirteen',
#     14:'fourteen',
#     15:'fifteen',
#     16:'sixteen',
#     17:'seventeen',
#     18:'eighteen',
#     19:'nineteen',
# }

# tens = {
#     2:'twenty',
#     3:'thirty',
#     4:'forty',
#     5:'fifty',
#     6:'sixty',
#     7:'seventy',
#     8:'eighty',
#     9:'ninety',
#     }

# while True:
#     x = int(input('Enter a number between 0 and 99: '))
#     if x < 0 or x > 99:
#         print('Please enter a number between 0 and 99.')
#     else:
#         break

# if x >= 10 and x < 20:
#     print(teens[x]) # printing between 10 and 19
# elif x >= 0 and x <= 9:
#     print(ones[x]) # printing between 0 and 9
# else: 
#     tens_digit = x // 10
#     ones_digit = x % 10 
#     print(tens[tens_digit] + ' ', ones[ones_digit])
#     # dividing x by 10 for tens digit / getting remainder (ie the ones digit) for ones
#     # ie 34... 34/10 = 3 and 4 is the remainder of that

# version 2 ---- #

ones = {
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
}

teens = {
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
}

tens = {
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}

while True:
    x = int(input('Enter a number between 0 and 999: '))
    if x < 0 or x > 999:
        print('Please enter a number between 0 and 999.')
    else:
        break

hundreds_digit = x // 100
tens_digit = x // 10 % 10 
ones_digit = x % 10 
teens_digit = x % 100 

if x >= 0 and x <= 9:
    print(ones[x]) # works
elif x >= 10 and x < 20:
    print(teens[x]) # works
elif x >= 21 and x <= 99:
    print(tens[tens_digit] + ' ', ones[ones_digit]) # works
elif x == 100 or x == 200 or x == 300 or x == 400 or x == 500 or x == 600 or x == 700 or x == 800 or x == 900:
    print(f'{ones[hundreds_digit]} hundred') # works
elif tens_digit == 1 and x > 100:
    print(f'{ones[hundreds_digit]} hundred {teens[teens_digit]}')
else:
    if x >= 101 and x <= 999: # i.e. 11
        print(f'{ones[hundreds_digit]} hundred {tens[tens_digit]} {ones[ones_digit]}') # works
