
def peaks(data):
    result = []

    for i in range(1, len(data) - 1):
        if(data[i] > data[i - 1] and data[i] > data[i + 1]):
           result.append(i)
    
    return result

def valleys(data):
    result = []

    for i in range(1, len(data) - 1):
        if(data[i] < data[i - 1] and data[i] < data[i + 1]):
           result.append(i)
    
    return result

def peaks_And_Valleys(data, peaks, valleys):
    new_Data = []
    new_List = []

    for i in data:
        new_Data.append('')
    for peak in peaks:
        new_Data[peak] = "P"
    for valley in valleys:
        new_Data[valley] = "V"
    
    print(new_Data)

    new_List = peaks + valleys
    return sorted(new_List)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def versionTwo(data):

    for col in range(max(data), 0, -1):
        for row in range(len(data)):
            if(data[row] >= col):
                print('x', end ='  ')
            else:
                print(' ', end ='  ')

def versionThree(data):
    for col in range(max(data), 0, -1):
        temp_Max = 0
        for row in range(len(data)):
            if(data[row] >= col):
                temp_Max = data[row]
                print('x', end ='  ')
            elif(data[row] < temp_Max):
                print('o', end ='  ')
            else:
                print(' ', end ='  ')


# print(peaks(data))
# print(valleys(data))
# print(peaks_And_Valleys(data, peaks(data), valleys(data)))

versionTwo(data)
print('\n')
versionThree(data)