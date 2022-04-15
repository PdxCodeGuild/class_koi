
def linear_search(arr, num):
    for i in range(len(arr)):
        if(arr[i] == num):
            return i
    return -1

def binary_search(arr, num):
    l = 0
    m = len(arr) // 2
    h = len(arr)

    while(True):
        if(num == arr[m]):
            return m
        elif(num < arr[m]):
            h = m
            m = h // 2
        elif(num > arr[m]):
            l = m
            m += (h - l) // 2
        elif(l > h):
            return -1

def binary_search_recurse(arr, num, l, h):
    if(l > h):
        return -1

    m = (l + h) // 2

    if(arr[m] == num):
        return m
    
    if(num > arr[m]):
        return binary_search_recurse(arr, num, m + 1, h)

    if(num < arr[m]):
        return binary_search_recurse(arr, num, l, m - 1)

test_arr = [1, 2, 3, 4, 5, 6, 7, 8]

# print(binary_search(test_arr, 0))

# arguments = (array, desired value, lowest index, highest index)
print(binary_search_recurse(test_arr, 7, 0, 8))
