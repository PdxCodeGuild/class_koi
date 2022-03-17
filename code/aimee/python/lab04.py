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

hundreds = {
    1:'one hundred',
    2:'two hundred',
    3:'three hundred',
    4:'four hundred',
    5:'five hundred',
    6:'six hundred',
    7:'seven hundred',
    8:'eight hundred',
    9:'nine hundred',
}

while True:
    x = int(input('Enter a number between 0 and 999: '))
    if x < 0 or x > 999:
        print('Please enter a number between 0 and 999.')
    else:
        break

if x % 100 >= 10 and x % 100 <= 20:
    hundreds_digit = x // 100
    print(hundreds[hundreds_digit] + teens[x]) # printing between 10 and 20, 110 and 120
elif x >= 0 and x <= 9:
    print(ones[x]) # printing between 0 and 9
else: # if x = 455
    hundreds_digit = x // 100 # 455 // 100 = 400
    x %= 100 # 455 % 100 = 55
    tens_digit = x // 10 # 455 // 10 = 45
    ones_digit = x % 10 # 455 % 10 = 5
     # if x were 300, dividing x by 100 would give the one digit - 3 + 'hundred'
    print(f'{ones[hundreds_digit]} hundred {tens[tens_digit]} {ones[ones_digit]}') # between 21 and 999
   













