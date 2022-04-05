
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = 1
        temp = 0
        while(arr[i - j] > arr[i]):
            if(i - j <= 0):
                break
            j += 1
        if(j > 1):
            temp = arr[i]
            arr.remove(arr[i])
            arr.insert(i - j, temp)
        print(arr)

list = [2,3,1,4,5,7,6,8,9]
insertion_sort(list)