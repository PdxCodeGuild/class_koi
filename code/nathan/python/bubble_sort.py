
def bubble_sort(arr):
    # how do we know that the list is sorted?
    sorted_flag = False
    while(sorted_flag == False):
        count = 0
        for i in range(len(arr) - 1):
            if(arr[i+1] < arr[i]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                count += 1
            print(count)
            # if no swaps have taken place, the list is sorted
        if(count == 0):
            sorted_flag = True
    print(arr)

list = [2,3,1,4,5,7,6,8,9,0]

bubble_sort(list)