'''
Python Lab 08: Credit Card Validation

- only one version
- this lab is pretty much done, just need to clean it up
- remove the print statements etc.
- also need to turn the whole thing into a function i guess.
'''

def get_number(): # requests a card number, rejects invalid entries
    while True:
        try:
            user_number = int(input('Enter your credit card number: ')) # convert input to int to get exceptions
            return str(user_number)
        except (ValueError, TypeError):
            print('that is an invalid entry.')

def credit_card_validation(credit_card_number):
    credit_card_number = [int(i) for i in credit_card_number] # TOPIC: Comprehensions, splits card number out into list

    check_number = credit_card_number.pop(-1) # pop off the last number

    credit_card_number.reverse() # reverse the card order

    for i in range(len(credit_card_number)): # iterate through the list by index
        if i % 2 == 0: # every other number
            credit_card_number[i] = credit_card_number[i] * 2 # multiple number by 2

    for i in range(len(credit_card_number)): # iterate through the list by index
        if credit_card_number[i] > 9: # if item at index is greater than 9 subtract 9
            credit_card_number[i] -= 9

    # credit_card_number = [n - 9 for n in credit_card_number if n > 9]

    sum_numbers = str(sum(credit_card_number)) # sum the items in the list, turn it into a string

    list(sum_numbers) # turn the string into a list

    sum_numbers = [int(i) for i in sum_numbers] # break out the string so i can check an individual value

    if sum_numbers[-1] == check_number:
        result = 'Valid!'
    else:
        result = 'Card number is invalid.'
    
    return result

user_card_number = get_number()

output = credit_card_validation(user_card_number)

print(output)


