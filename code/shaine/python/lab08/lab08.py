#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 8: Credit Card Validation
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


def card_check(card_number):

    '''write a function which returns whether a string 
    containing a credit card number is valid as a boolean.''' 

    # converts string input into a list
    card_num = list(card_number)

    for i in range(0, len(card_num)):
        # converts each string iin the list to an int
        card_num[i] = int(card_num[i])

    print(card_num)

    # pops last digit to save as check digit variable
    check_digit = card_num.pop(-1)
    print(check_digit)

    '''Reverse the digits.'''

    rev_digits = card_num[::-1]
    print(rev_digits)

    '''Double every other element in the reversed list.'''

    # doubles the every other value from the reversed list
    for i in range(0, len(rev_digits)):
        if i%2 == 0:
            num = int(rev_digits[i])
            double = num*2
            rev_digits[i] = double

    print(rev_digits)

    '''Subtract nine from numbers over nine.'''

    for i in range(0, len(rev_digits)):
        if rev_digits[i] > 9:
            sub = int(rev_digits[i])-9
            rev_digits[i] = sub

    print(rev_digits)

    '''Sum all values.'''

    sum_total = sum(rev_digits)

    print(sum_total)

    '''Take the second digit of that sum.'''

    string_sum = str(sum_total)

    second_digit = string_sum[1]

    print(second_digit)


    # If that matches the check digit, the whole card number is valid.

    if int(check_digit) == int(second_digit):
        return print("valid")
    else:
        return print("invalid")

#  inputs the card number
card_number = input('Enter card number: ')
# runs the card number through the card check function
verify = card_check(card_number)
