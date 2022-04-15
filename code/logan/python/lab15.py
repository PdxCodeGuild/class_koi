## Lab 15 ##
## Code ##

# sample = [1, 2, 3, 4, 5, 6, 7, 8,]
usample = [8, 7, 5, 6, 1, 3, 2, 4]

## Part 1 ##
## Linear Search ##

# def linear_search(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return i
#     return None


## Part 2 ##
## Binary Search ##


# def binary_search(data, target):
#     low = 0
#     high = len(data) - 1
#     while low < high:
#         middle = (low + high) // 2
#         if data[middle] < target:
#             low = middle + 1
#         elif data[middle] > target:
#             high = middle - 1
#         else:
#             return middle
#     return None


## Part 3 ##
## Bubble Sort ##
# def bubblesort(data):
#     while True:
#         swapped = False
#         for i in range(1,len(data)):
#             if data[i - 1] > data[i]:
                # current = data[i]
                # previous = data[i -1]
                # data[i - 1] = current
                # data[i] = previous
#                 swapped = True
#         if swapped == False:
#             break
#     return data

## Part 4 ##
## Insertion Sort ##
def insertion_sort(data):
    i = 1
    while i < len(data):
        j = i
        while j > 0 and (data[j-1] > data[j]):
            current = data[j]
            previous = data[j-1]
            data[j] = previous
            data[j-1] = current
            j -= 1
        i += 1
    return data




## Debugging

# index = linear_search(sample, 7)
# index = binary_search(sample, 7)
# sorted = bubblesort(usample)
sorted = insertion_sort(usample)
# sorted = insertion_sort(sample)

# print(index)
print(sorted)