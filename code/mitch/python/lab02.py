# Lab 2: Average Numbers
# Mitch Chapman


### Version 1 ----------------------------------------------------
nums = [5, 0, 8, 3, 4, 1, 6]

# looping over the numbers in nums adding to running sum each loop
running_sum = 0
for num in nums:
    running_sum += num

average = running_sum / len(nums)

print(f"\nThe average of the numbers {nums} is {average}.\n")



### Version 2 -----------------------------------------------------
nums = []
running_sum = 0

#while loop adding numbers to list of numbers and adding to running sum; breaking when 'done' is entered
while True:
    user_input = input("Enter a number or 'done': ")
    if user_input == 'done':
        break
    else:
        nums.append(int(user_input))
        running_sum += int(user_input)

average = running_sum / len(nums)

print(f"The average of the numbers {nums} is {average}.")




