print('\nWelcome to the Credit Card Validator.')

card_num = input('\nPlease enter, the sixteen digit credit card number to validate:')

cred_card_test = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'

def cred_card_valid(card_num):
    
    list_ints = list(card_num)
    print(list_ints)

cred_card_valid(card_num)

