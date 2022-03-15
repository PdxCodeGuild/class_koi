'''
PDX Code Guild - Class Koi
Lab 02 - Average Numbers
Matt Walsh
'''

""" 
# Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
num_sum = 0

# loop over the elements and add each number to num_sum variable
for num in nums:
    num_sum += num 

# divide sum of numbers by length of list
print(f'The average of {nums} is {num_sum / len(nums)}.')
"""

# Version 2

nums = [] # empty list for user-input numbers to be added to
num_sum = 0 # varible for running total

while True:
    user_entry = input('Please enter a number, or type \'done\' to see the result and quit: ')
    try:
        nums.append(float(user_entry)) # append user_entry to nums list as float if no error is generated
    except:
        if user_entry == 'done': # if appending failed, check to see if the user entered 'done'
            for num in nums: # loop through numbers and add to running total
                num_sum += num
            print(f'The average of {nums} is {num_sum / len(nums)}.') # print results
            break
        else: # if appending failed and the user did not enter 'done', display an error message
            print('I didn\'t recognize that input. Please try again.')
