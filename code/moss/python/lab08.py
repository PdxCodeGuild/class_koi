print('\nWelcome to the Credit Card Validator.')

# card_num = input('''\nPlease enter, 
# the sixteen digit credit card number to validate:''')

cred_card_test = '4556737586899855'

def cred_card_valid(cred_card_test):
    #1
    list_ints = list(cred_card_test)
    for i in range(len(list_ints)):
        list_ints[i] = int(list_ints[i])
    print(f'\n1.{list_ints}.')
    #2
    chk_digit = list_ints.pop()
    # print(chk_digit)
    print(f'\n2.{list_ints}.')
    #3
    reversed_digit = list(reversed(list_ints))
    print(f'\n3.{reversed_digit}.')
    #4
    for i in range(0,len(reversed_digit),2):
        reversed_digit[i] *=2
    print(f'\n4.{reversed_digit}.')









cred_card_valid(cred_card_test)

