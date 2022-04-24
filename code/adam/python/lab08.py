# Lab 08 - Credit Card Validation function
   
# function to validate credit card input string
def credit_card_validation(cc_num_str):
    # Convert the input string of numbers into a list of ints
    credit_card_list = []
    for num in credit_card_str:
        credit_card_list.append(int(num))
    # Slice off the last digit. That is the check digit.
    check_digit = credit_card_list.pop(-1)
    # Reverse the digits.
    credit_card_list.reverse()
    # Double every other element in the reversed list.
    for i, num in enumerate(credit_card_list):
        if i % 2 == 0:
            credit_card_list[i] *= 2
    # Subtract nine from numbers over nine.
    for i, num in enumerate(credit_card_list):
        if credit_card_list[i] > 9:
            credit_card_list[i] -= 9
    # Sum all values.
    sum_of_list = sum(credit_card_list)
    # Take the second digit of that sum.
    second_digit = int(str(sum_of_list)[1])
    # If that matches the check digit, the whole card number is valid.
    if second_digit == check_digit:
        print('Credit Card number is Valid!')
    else:
        print('Credit Card number is In-Valid')

# request credit card number from user
credit_card_str = input("Enter the 16-digit credit card number: ")

# call function and run input string of credit card number
credit_card_validation(credit_card_str)
