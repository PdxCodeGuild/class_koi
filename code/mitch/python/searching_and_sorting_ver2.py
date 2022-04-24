# Lab 15: Searching and Sorting
# Version 1
# Mitch Chapman


def linear_search(nums:list, value:int):
    """Loops through list of values and returns the index position of the value 
    input."""
    
    for i, num in enumerate(nums):
        if num == value:
            return i
    return None


nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = 7
index = linear_search(nums=nums, value=value)
print(f"The index of the value '{value}' was {[index] if index is not None else 'not found; value not in the list of numbers'}. This index was identified using a linear search.")




def binary_search(nums:list, value:int):
    """Defines lowest and highest index positions, then compares the middle inxex to 
    value input, then redefines high and low index to capture and hone in on index 
    of value. Finally returns index position of value if present or None if not present."""
    
    sorted_nums = sorted(nums)
    low_i = 0
    high_i = len(sorted_nums)-1
    if sorted_nums[low_i] == value:
        return low_i
    elif sorted_nums[high_i] == value:
        return high_i
    else:
        while low_i < high_i:
            middle_i = (low_i + high_i) // 2
            if sorted_nums[middle_i] < value:
                low_i = middle_i + 1
            elif sorted_nums[middle_i] > value:
                high_i = middle_i - 1
            else:
                return middle_i
    return None


nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = 7
index = binary_search(nums=nums, value=value)
print(f"The index of the value '{value}' was {[index] if index is not None else 'not found; value not in the list of numbers'}. This index was identified using a binary search.")












