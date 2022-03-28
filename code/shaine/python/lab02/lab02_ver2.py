#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 2: Average Numbers 
#       Version: 2
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# Ask the user to enter the numbers one at a time, putting them into a list. 
# If the user enters 'done', then calculate and display the average.


user_list = []

while True:
    user_nums = input("enter a number, or 'done': ")

    if user_nums != 'done':
        user_list.append(int(user_nums))
        continue

    elif user_nums == 'done':
        sum = 0

        for num in user_list:
            sum  += num
            
        total = sum/len(user_list)
        print(f'average: {total}')
        break
    
