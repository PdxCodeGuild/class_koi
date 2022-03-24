'''
Class Koi, Lab 2: Average Numbers

We are going to average a list of numbers.
'''

nums = []

user_input = input('enter a number, or \"done\": ')

while user_input != "done":
    try:
        user_input = float(user_input)
        nums.append(user_input)
    except ValueError:
        print('that is not a numerical value.')
    user_input = input('enter a number, or \"done\": ')

if user_input == "done":
    # print(nums)
    average = sum(nums) / len(nums)
    print(average)