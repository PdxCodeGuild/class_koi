#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 2: Average Numbers 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# average a list of numbers
nums = [5, 0, 8, 3, 4, 1, 6]

# iterate through it, keeping a 'running sum', 
sum = 0

for num in nums:
    sum  += num
    
# then divide that sum by the number of elements in that list

total = sum/len(nums)

print(round(total, 4))

