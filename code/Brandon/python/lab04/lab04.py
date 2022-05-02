
single_digit = {
    0 : '',
    1 : 'one', 
    2 : 'two', 
    3 : 'three',
    4 : 'four',
    5 : 'five', 
    6 : 'six', 
    7 : 'seven', 
    8 : 'eight', 
    9 : 'nine',
}

double_digit = { 
    0 : 'ten',
    1 : 'eleven',
    2 : 'twelve',
    3 : 'thirteen',
    4 : 'fourteen',
    5 : 'fifteen',
    6 : 'sixteen',
    7 : 'seventeen',
    8 : 'eighteen',
    9 : 'nineteen',
    }

tens = {
    0 : '',
    1 : 'eleven',
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'Ninety'
}
x = int(input('Please enter a number 1-999 to convert: '))

tens_digit = x//10 %10
ones_digit = x%10
hundreths = x//100 

if x >= 1 and x <=9:
    print(single_digit[x])

if x >= 10 and x <= 19:
    print(double_digit[x])

if x >= 20 and x <= 99:
    print(tens[tens_digit], single_digit[ones_digit])

if x >= 100 and x <= 999 and ones_digit != 0 and tens_digit != 1 and tens_digit != 0:
    print(single_digit[hundreths],'hundred', tens[tens_digit], single_digit[ones_digit])

elif ones_digit == 0:
    print(single_digit[hundreths],'hundred and', tens[tens_digit])

elif tens_digit == 1:
    print(single_digit[hundreths],'hundred', tens[tens_digit])

elif tens_digit == 0:
    print(single_digit[hundreths],'hundred and', single_digit[ones_digit])

# issues with 111, 404, 280 anytime there was a 0 in tens and ones