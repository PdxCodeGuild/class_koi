print('\nWelcome to the Credit Card Validator.')

# card_num = input('''\nPlease enter, 
# the sixteen digit credit card number to validate:''')

cred_card_test = '4556737586899855'

def cred_card_valid(cred_card_test):
    
    #1. Convert the input string into a list of ints
    list_ints = list(cred_card_test)
    for i in range(len(list_ints)):
        list_ints[i] = int(list_ints[i])
    print(f'\n1.{list_ints}.')
    
    #2. Slice off the last digit. That is the check digit.
    chek_digit = list_ints.pop()
    # print(chk_digit)
    print(f'\n2.{list_ints}.')
    
    #3. Reverse the digits.
    reversed_digit = list(reversed(list_ints))
    print(f'\n3.{reversed_digit}.')
    
    #4. Double every other element in the reversed list.
    for i in range(0,len(reversed_digit),2):
        reversed_digit[i] *=2
    print(f'\n4.{reversed_digit}.')
    
    #5. Subtract nine from numbers over nine.
    for i in range(len(reversed_digit)):
        if reversed_digit[i] > 9:
            reversed_digit[i] -= 9
    print(f'\n5.{reversed_digit}.')
    
    #6. Sum all values.
    sum = 0
    for num in reversed_digit:
        sum += num
    print(f'\n6. {sum}.')
    
    #7. Take the second digit of that sum.
    second_digit = sum % 10
    print(f'\n7. {second_digit}.')

    #8. If that matches the check digit, the whole card number is valid.
    if second_digit == chek_digit:
        print(f'\n8. Credit Card is VALIDATED.\n')

cred_card_valid(cred_card_test)

