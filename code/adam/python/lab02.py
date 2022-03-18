# Lab 02 Average Numbers
#----------------------------------------------------------------------------------------
'''
# Version 1 - Use hard coded list

# define list of numbers
numbers = [5, 0, 8, 3, 4, 1, 6]

# create function that will iteratively sum the numbers list
def sum_of_list(nums) :
    # define variable to hold cumulative sum and start at zero
    sum_total = 0
    # loop over elements in list 
    for num in numbers:
        sum_total += num
    return sum_total
# call function to sum list of numbers saving to summation variable
summation = sum_of_list(numbers)
# determine how many numbers are in the list save as quantity
quantity = len(numbers)
# find the average of the list of numbers
ave_list = summation / quantity

print(ave_list)
'''
#-------------------------------------------------------------------------------------------------
# Version 2 - allow users to enter numbers one at a time

# define an empty list of numbers to populate with user input
numbers = []

# create while loop to get numbers from user with option to exit
while True:
    #get number from user to append to list
    new_number = input("Please enter a number or 'done' to quit: ")
    if new_number == 'done':
        break
    # change input string to integer and append to list
    else:
        new_number = int(new_number)
        numbers.append(new_number)
# create function to find sum of list of numbers
def sum_of_list(nums) :
    # define variable to hold cumulative sum and start at zero
    sum_total = 0
    # loop over elements in list 
    for num in numbers:
        sum_total += num
    return sum_total
# find the length of the list of numbers
quantity = len(numbers)
# call function to get sum of list
sum_total = sum_of_list(numbers)
# get average of list of numbers
ave_list = sum_total / quantity

print(f'''average: {ave_list}''')
