''' 
Lab 4: Number to Phrase
'''

numbers_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

teens_dict = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

tens_dict = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

def get_number():
    while True:
        try:
            user_number = input('enter an integer: ')
            if int(user_number) > 999 or int(user_number) < 0:
                print('that is an invalid entry.')
            else:
                return int(user_number)
        except (ValueError, TypeError):
            print('that is an invalid entry.')

user_number = get_number()

hundreds_digit = user_number // 100

tens_digit = ((user_number // 10) - (hundreds_digit * 10))

ones_digit = user_number % 10

if hundreds_digit >= 1 and tens_digit > 1 and ones_digit != 0: # ex 122 -> one hundred twenty two
    print(f'{numbers_dict[hundreds_digit]} hundred {tens_dict[tens_digit]} {numbers_dict[ones_digit]}')
elif hundreds_digit >= 1 and tens_digit == 1 and ones_digit != 0: # ex 111 -> one hundred eleven
    print(f'{numbers_dict[hundreds_digit]} hundred {teens_dict[ones_digit]}')
elif hundreds_digit >= 1 and tens_digit >= 1 and ones_digit == 0: # ex 120
    print(f'{numbers_dict[hundreds_digit]} hundred {tens_dict[tens_digit]}')
elif hundreds_digit >= 1 and tens_digit == 0 and ones_digit == 0: # ex 100
    print(f'{numbers_dict[hundreds_digit]} hundred')
elif hundreds_digit < 1 and tens_digit > 1 and ones_digit != 0: # ex 99
    print(tens_dict[tens_digit], numbers_dict[ones_digit])
elif hundreds_digit < 1 and tens_digit > 1 and ones_digit == 0: # ex 20
    print(tens_dict[tens_digit])
elif hundreds_digit < 1 and tens_digit == 1: # ex 11 -> eleven
    print(teens_dict[ones_digit])
elif hundreds_digit < 1 and tens_digit == 0: # 1 -> one
    print(numbers_dict[ones_digit])