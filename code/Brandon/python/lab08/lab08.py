# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

user_list = 4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5


def string_converter():
    numbers = []

    for i in user_list:
        numbers.append(i)
    
    
    check_digit = numbers[15]
    numbers = numbers[:-1]

    numbers.reverse()
    print(numbers)

    numbers[0] = numbers[0] * 2
    numbers[2] = numbers[2] * 2
    numbers[4] = numbers[4] * 2
    numbers[6] = numbers[6] * 2
    numbers[8] = numbers[8] * 2
    numbers[10] = numbers[10] * 2
    numbers[12] = numbers[12] * 2
    numbers[14] = numbers[14] * 2
    print(numbers)
    
    for i in range(len(numbers)):
        if numbers[i] > 9:
            numbers[i] = numbers[i] - 9
    
    print(numbers)

    numbers = sum(numbers)
   
    numbers = numbers % 10

    if numbers%10 == check_digit:
        print("Valid!")
    else:
        print("Invalid number, please try again")    
    print(check_digit)
        
    print(type(numbers))
    print(numbers)
    
string_converter()