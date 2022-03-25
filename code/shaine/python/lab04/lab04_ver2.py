#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 4: Number to Phrase
#       Version: 2.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# Handle numbers from 0-999

user_num = int(input('Enter a number from 0-999: '))

low_num_dict = {
0:'zero',
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',}

high_num_dict = {
2:'twenty',
3:'thirty',
4:'forty',
5:'fifty', 
6:'sixty', 
7:'seventy', 
8:'eighty',
9:'ninety'}



if user_num < 20:
    print(f'Your number is {low_num_dict[user_num]}')
elif user_num < 100:
    tens_digit = user_num//10
    ones_digit = user_num%10
    if ones_digit == 0:
        print(f'Your number is {high_num_dict[tens_digit]}')
    else:
        print(f'Your number is {high_num_dict[tens_digit]}-{low_num_dict[ones_digit]}')

elif user_num > 99:
    hunds_digit = user_num//100
    tens_digit = (user_num%100)//10
    ones_digit = (user_num%100)%10   

    if tens_digit == 0 and ones_digit == 0:
        print(f'Your number is {low_num_dict[hunds_digit]}-hundred')
    
    elif tens_digit == 0:
        print(f'Your number is {low_num_dict[hunds_digit]}-hundred and {low_num_dict[ones_digit]}')

    elif tens_digit == 1:
        new_tens_digit = user_num%100
        print(f'Your number is {low_num_dict[hunds_digit]}-hundred and {low_num_dict[new_tens_digit]}')

    elif ones_digit == 0:
        print(f'Your number is {low_num_dict[hunds_digit]}-hundred {high_num_dict[tens_digit]}')

    else:
        print(f'Your number is {low_num_dict[hunds_digit]}-hundred {high_num_dict[tens_digit]}-{low_num_dict[ones_digit]}')

