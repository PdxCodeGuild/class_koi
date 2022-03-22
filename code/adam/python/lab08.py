# Lab 08 - Credit Card Validation

# request credit card number from user
credit_card_str = input("Enter the credit card number: ")
# function to validate credit card input string
# def credit_card_validation():

# Convert the input string of numbers into a list of ints
credit_card_list = []
for num in credit_card_str:
    credit_card_list.append(int(num))

# Slice off the last digit. That is the check digit.
check_digit = credit_card_list.pop(-1)

# Reverse the digits.
credit_card_reversed = credit_card_list.copy()
print(f'cc list before {credit_card_list}')
credit_card_reversed.reverse()
# credit_card_list_reversed.reverse()

# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
print(f'cc list after {credit_card_list}')
print(f'credit card string: {credit_card_str}')
print(f'cc reversed after {credit_card_reversed}')
# print(credit_card_list_reversed)
print(id(credit_card_reversed))
print(id(credit_card_list))