# lab 08, credit card validation ---- #

def validation(user_input):
    user_input = ('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5')
    user_input = user_input.split()
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])

    credit_card = user_input[:-1]

    credit_card.reverse()

    for i in range(len(credit_card)):
        if i % 2 == 0:
            credit_card[i] = credit_card[i] * 2

    for i in range(len(credit_card)):
        if credit_card[i] > 9: 
            credit_card[i] = credit_card[i] - 9

    total = sum(credit_card)

    digits = [int(x) for x in str(total)] # converts number to string then int

    if True:
        if digits[1] == user_input[15]:
            return 'Valid'

print(validation('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'))
