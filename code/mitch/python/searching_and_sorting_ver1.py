# Lab 15: Searching and Sorting
# Version 1
# Mitch Chapman


def linear_search(nums:list, value:int):
    """Loops through list of values and returns the index position of the value input."""
    for i, num in enumerate(nums):
        if num == value:
            return i
    return None


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums=nums, value=7)
print(index)
















