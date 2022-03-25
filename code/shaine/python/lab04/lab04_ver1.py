#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 4: Number to Phrase
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# Convert a given number into its english representation. 
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# 1-19 will have to be individual 
# use an if/else to see if the number is < 20


user_num = int(input('Enter a number from 0-99: '))

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
elif user_num >= 20:
    tens_digit = user_num//10
    ones_digit = user_num%10
    print(f'You number is {high_num_dict[tens_digit]}-{low_num_dict[ones_digit]}')












