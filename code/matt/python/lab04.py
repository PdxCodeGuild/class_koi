'''
PDX Code Guild - Class Koi
Lab 04 - Number to Phrase
Matt Walsh
'''

 
# Version 1
"""
#  dictionaries for text versions of numbers
ones_names = {
    0:'',
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

tens_names = {
    0:'',
    1:'ten',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}

teens_names = {
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

while True:  # validation to check if the input is an integer and within range
    x = input("Please enter a number between 0 and 99: ")
    try:
        x = int(x)
        if x < 0 or x > 99:
            print('I\'m sorry, that number is outside of the range of 0-99. Try again.')
        else:
            break
    except:
        print('I\'m sorry, that isn\'t a number. Try again.')


if x == 0: # print zeroes 
    print('zero')
elif x > 10 and x < 20: # print teens
    print(teens_names[x])
else: # use floor division and modulus to determine tens and ones values
    tens = x // 10
    ones = x % 10
    print(tens_names[tens] + ones_names[ones] if tens == 0 or ones == 0 else tens_names[tens] + '-' + ones_names[ones]) # use tens and ones values as dictionary keys and an if statement to add hyphen where necessary
"""

# Version 2
""" 
#  dictionaries for text versions of numbers
ones_names = {
    0:'',
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

tens_names = {
    0:'',
    1:'ten',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}

teens_names = {
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

while True: # validation to check if the input is an integer and within range
    x = input("Please enter a number between 0 and 999: ")
    try:
        x = int(x)
        if x < 0 or x > 999:
            print('I\'m sorry, that number is outside of the range of 0-999. Try again.')
        else:
            break
    except:
        print('I\'m sorry, that isn\'t a number. Try again.')


if x == 0: # print zeroes
    print('zero')
elif x % 100 > 10 and x % 100 < 20: # print teens and hundred-teens
    hundreds = x // 100
    print((ones_names[hundreds] + '-hundred ' if hundreds != 0 else '') + teens_names[x % 100]) # if statement returns empty string if the number is less than 100 but will still print teen name
else: # use floor division and modulus to determine hundreds, tens, and ones values
    hundreds = x // 100
    x %= 100
    tens = x // 10
    ones = x % 10
    print((ones_names[hundreds] + '-hundred ' if hundreds != 0 else '')  + (tens_names[tens] + ones_names[ones] if tens == 0 or ones == 0 else tens_names[tens] + '-' + ones_names[ones])) # use tens and ones values as dictionary keys and if statements to add hyphen where necessary and include hundreds where necessary
"""

# Version 3
""" 
#  dictionaries for roman numeral versions of numbers
roman = {
    900:'CM',
    500:'D',
    400:'CD',
    100:'C',
    90:'XC',
    50:'L',
    40:'XL',
    10:'X',
    9:'IX',
    5:'V',
    4:'IV',
    1:'I'
}

while True: # validation to check if the input is an integer and within range
    x = input("Please enter a number between 0 and 999: ")
    try:
        x = int(x)
        if x < 0 or x > 999:
            print('I\'m sorry, that number is outside of the range of 0-999. Try again.')
        else:
            break
    except:
        print('I\'m sorry, that isn\'t a number. Try again.')

answer = '' # empty string for result

for numeral in roman: # loop through each entry in dictionary
    while x - numeral >= 0: # keep looping as long as the result won't be less than 0
        answer += roman[numeral] # add roman numeral to answer string
        x -= numeral # subtract value from user input

print(answer) # print results
"""

# Version 4


#  dictionaries for text versions of numbers
ones_names = {
    0:'',
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

tens_names = {
    0:'',
    1:'ten',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
}

teens_names = {
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

while True:  # validation to check if the input is a valid time
    x = input("Please enter a time formatted like 12:00: ")
    try:
        x = x.split(':')
        x[0] = int(x[0])
        x[1] = int(x[1])
        if x[0] < 0 or x[1] < 0 or x[0] > 12 or x[1] > 59:
            print('I\'m sorry, that number is not a valid time. Try again.')
        else:
            break
    except:
        print('I\'m sorry, that number is not a valid time. Try again.')

for each in x:
    if each == 0: # print o'clock for hours 
        print('o\'clock')
    elif each > 10 and each < 20: # print teens
        print(teens_names[each], end=' ')
    else: # use floor division and modulus to determine tens and ones values
        tens = each // 10
        ones = each % 10
        print(tens_names[tens] + ones_names[ones] if tens == 0 or ones == 0 else tens_names[tens] + '-' + ones_names[ones], end=' ') # use tens and ones values as dictionary keys and an if statement to add hyphen where necessary