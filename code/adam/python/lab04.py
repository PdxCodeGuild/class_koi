# Lab 04 - Number to Phrase
# Version 2 - Accept numbers 0-999

# get number from user and convert to integer
number = int(input('Please enter a number between 0-999: '))
# creat list of english numbers 'one' thru 'ninteen'
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
# create english list of tens 'twenty' thru 'ninety' 
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
# create english list of hundreds, 'one-hundred' thru 'nine-hundred'
hundreds_list = [
    '',
    'one-hundred',
    'two-hundred',
    'three-hundred',
    'four-hundred',
    'five-hundred',
    'six-hundred',
    'seven-hundred',
    'eight-hundred',
    'nine-hundred',
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
    if ones_digit == 0:
        print(f'{tens_list[tens_digit]}{ones_list[ones_digit]}')
    else:
        print(f'{tens_list[tens_digit]}-{ones_list[ones_digit]}')
elif number <= 999:
    hundreds_digit = number//100
    tens_digit = number%100//10
    ones_digit = number%100%10
    if ones_digit == 0:
        print(f'{hundreds_list[hundreds_digit]} {tens_list[tens_digit]}{ones_list[ones_digit]}')
    else:
        print(f'{hundreds_list[hundreds_digit]} {tens_list[tens_digit]}-{ones_list[ones_digit]}')
else:
    print(f'Sorry, but the number "{number}" was not between 0-999')


