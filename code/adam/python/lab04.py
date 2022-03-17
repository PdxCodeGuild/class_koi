# Lab 04 - Number to Phrase
# Version 1 - Accept numbers 0-99

# get number from user and convert to integer
number = int(input('Please enter a number between 0-99: '))
# creat list of english numbers one thru ninteen
ones_list = [
    '', 
    'one', 
    'two', 
    'three', 
    'four', 
    'five', 
    'six', 
    'seven', 
    'eight', 
    'nine', 
    'ten', 
    'eleven', 
    'twelve', 
    'thirteen', 
    'fourteen', 
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]
# create english list of tens, twenty thru ninety 
tens_list = [
    '',
    '',
    'twenty',
    'thirty',
    'fourty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]
# print users inputed number
print(number)

# output zero for '0' input
if number == 0:
    print('zero')
# output for input '1' thru '19'
elif number <= 19:
    print(ones_list[number])
# output for input '20' thru '99'
elif number <= 99:
    tens_digit = number//10
    ones_digit = number%10
    print(f'{tens_list[tens_digit]}{ones_list[ones_digit]}')
else:
    print(f'Sorry, but the number "{number}" was not between 0-99')


