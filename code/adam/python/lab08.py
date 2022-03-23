# Lab 08 - Credit Card Validation

# request credit card number from user
credit_card_str = input("Enter the 16-digit credit card number: ")
    
# function to validate credit card input string
# def credit_card_validation():

# Convert the input string of numbers into a list of ints
credit_card_list = []
for num in credit_card_str:
    credit_card_list.append(int(num))

# Slice off the last digit. That is the check digit.
check_digit = credit_card_list.pop(-1)

# Reverse the digits.
credit_card_list.reverse()

# Double every other element in the reversed list.
# i = 0
for i in credit_card_list:
    credit_card_list[i] = credit_card_list[i] + credit_card_list[i]
# credit_card_list[0] = credit_card_list[0] * 2
# credit_card_list[2] = credit_card_list[2] * 2
# credit_card_list[4] = credit_card_list[4] * 2
# credit_card_list[6] = credit_card_list[6] * 2
# credit_card_list[8] = credit_card_list[8] * 2
# credit_card_list[10] = credit_card_list[10] * 2
# credit_card_list[12] = credit_card_list[12] * 2
# credit_card_list[14] = credit_card_list[14] * 2

# Subtract nine from numbers over nine.
# if credit_card_list[0] > 9:
#     credit_card_list[0] = credit_card_list[0] - 9


# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
print(credit_card_list)