'''
PDX Code Guild - Class Koi
Lab 15 - Searching and Sorting
Matt Walsh
'''


# Part 1- Linear Search
'''
def linear_search(nums, value):
    """
    Uses linear search to find a value in a list
    """
    # return str(nums.index(value))
    try:
        return nums.index(value)
    except:
        return False

# list of numbers and number to search for
nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = 7
# assign search to variable
index = linear_search(nums, value)

# display "not found" message if not in list
if not index:
    print(f'{value} was not found.')
# display position if found
else:
    print(f'{value} was located at index {index}')
'''


# Part 2 - Binary Search
'''
def binary_search(nums, value):
    """
    Uses binary search to find values in a list
    """
    # finds length of list and assigns variables for leftmost and rightmost positions
    nums_len = len(nums)
    l = 0
    r = nums_len - 1

    while l <= r:
        # finds middle position
        m = (l + r) // 2
        if nums[m] < value:
            l = m + 1
        elif nums[m] > value:
            r = m - 1
        else:
            return f'{value} was located at index {m}'
    return f'{value} was not found.'


# list of numbers and number to search for
nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = 7
# assign results to variable and display
index = binary_search(nums, value)
print(index)
'''


# Part 3 - Bubble Sort
'''
def bubble_sort(nums):
    """
    Sorts a list using bubble sort method
    """
    # find length of nums list
    n = len(nums)
    # set swapped variable to True for while loop
    swapped = True
    while swapped:
        # set swapped variable to False so while loop will end if value not swapped
        swapped = False
        # iterate through list starting at second position
        for i in range(1,n):
            # swap positions if the previous value is greater than the current value
            if nums[i - 1] > nums[i]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                # set swapped variable back to True so the loop continues
                swapped = True
    # once complete, return the sorted list
    return nums

# assign and display unsorted list
nums = [5,3,7,1,6,8,2,4]
print('Unsorted list: ', nums)

# assign sorted version to variable
nums = bubble_sort(nums)

# display sorted list
print('Sorted list: ',nums)
'''


# Part 4 - Insertion Sort
'''
def insertion_sort(nums):
    """
    Sorts a list using insertion sort method
    """
    # set i to 1
    i = 1
    # loop as long as i is less than the length of nums
    while i < len(nums):
        # set j to match i
        j = i
        # loop as long as j is greater than 0 and the previous value is greater than the current value
        while j > 0 and nums[j - 1] > nums[j]:
            # move the lower value to the left
            nums[j],nums[j-1] = nums[j-1],nums[j]
            # decrement j to continue moving the lower tem to the right as needed
            j -= 1
        # increment i to check the next position
        i += 1
    # return sorted list
    return nums

# assign and display unsorted list
nums = [5,3,7,1,6,8,2,4]
print('Unsorted list: ', nums)

# assign sorted version to variable
nums = insertion_sort(nums)

# display sorted list
print('Sorted list: ',nums)
'''


# Part 5 - Quicksort

def quicksort(nums):
    """
    Initializes quicksort method
    """
    quicksort_recursive(nums,0,len(nums) - 1)
    return nums

def quicksort_recursive(nums,start,end):
    """
    Sorts a list using quicksort method
    """
    if start < end:
        # set partition npoint
        partition = quicksort_partition(nums,start,end)
        # pass list, start point, and partition back into this function
        quicksort_recursive(nums,start,partition)
        # pass list, new partition, and end point back into this function
        quicksort_recursive(nums,partition + 1,end)

def quicksort_partition(nums,start,end):
    """
    Assigns partition for quicksort
    """
    # set pivot point
    pivot = nums[start + (end - start) // 2]
    # set i & j to match start & end point
    i = start
    j = end
    while True:
        # in/decrement i & j based on comparison to pivot
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        # return j once it is greater than or equal to i
        if i >= j:
            return j
        # swap positions
        nums[i], nums[j] = nums[j], nums[i]


# assign and display unsorted list
nums = [5,3,7,1,6,8,2,4]
print('Unsorted list: ', nums)

# assign sorted version to variable
nums = quicksort(nums)

# display sorted list
print('Sorted list: ',nums)