
single_digit = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

double_digit = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'Ninety'
}
user_input = int(input('Please enter a number 1-999 to convert: '))

x = user_input

if x >= 1 and x <= 9:
    print(single_digit[x])

if x >= 10 and x <= 19:
    print(double_digit[x])

if x >= 20 and x <= 99:
    tens_digit = x//10
    ones_digit = x % 10
    print(tens_digit)
    print(tens[tens_digit], single_digit[ones_digit])

if x >= 100 and x <= 999:
    tens_digit = x//10 % 10
    ones_digit = x % 10
    hundreths = x//100

    print(single_digit[hundreths], 'hundred',
          tens[tens_digit], single_digit[ones_digit])
