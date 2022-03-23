# Lab 09 - Peaks and Valleys

data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
# define function 'peaks' 
# -Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks (data):
    peaks_index_list = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks_index_list.append(i)
    return peaks_index_list

# print(peaks(data))

# define function 'valleys'
# -Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
def valleys(data):
    valleys_index_list = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys_index_list.append(i)
    return valleys_index_list

# print(valleys(data))

# define function peaks_and_valleys
# -uses the above two functions to compile a single list of the peaks and valleys 
# -in order of appearance in the original data.
def peaks_and_valleys():
    peaks_and_valleys_list = peaks(data) + valleys(data)
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list

# print(peaks_and_valleys())

#---------------------------------------------------------------------------------------

# max_data = max(data)
# print(max_data)
# print(data)
# print(data.count(9))

data_list = list(enumerate(data))
# print(data_list)
# for i in data_list:
#     print(i)

# print(data_list[0])

print('x'*8,'','x')
xxxxxxxx  xx
