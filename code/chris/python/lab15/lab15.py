'''
Lab 15: Searching and Sorting

- Linear Search O(n) DONE
- Binary Search DONE
- Bubble Sort (optional)
- Insertion Sort (optional)
- Quicksort (optional)
'''

import random

rand_value = random.randint(1, 8)
print('random value: ', rand_value)

# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]

print('---Linear Search---')

def linear_search(number_list, value):
    for num in number_list:
        if value == num:
            return nums.index(num)

index = linear_search(nums, rand_value)
print('linear index: ', index) # 6

print('---Binary Search---')

def binary_search(number_list, random_value):
    number_list.sort()
    high = len(nums) - 1
    low = 0
    while low < high:
        mid = (high + low) // 2
        if nums[mid] == random_value:
            return mid
        elif nums[mid] < random_value:
            low = mid
        elif nums[mid] > random_value:
            high = mid

binary_index = binary_search(nums, rand_value)
print('binary index: ', binary_index)
