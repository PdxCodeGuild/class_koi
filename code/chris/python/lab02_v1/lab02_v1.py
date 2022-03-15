'''
Class Koi, Lab 2: Average Numbers

Version 1

We are going to average a list of numbers.
'''

nums = [5, 0, 8, 3, 4, 1, 6]

nums_sum = 0

for i in range(len(nums)):
    nums_sum += nums[i]

nums_average = nums_sum / len(nums)
print(f"average: {nums_average}")