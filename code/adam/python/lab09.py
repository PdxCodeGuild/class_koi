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

print(f'Peaks: {peaks(data)}')

# define function 'valleys'
# -Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
def valleys(data):
    valleys_index_list = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys_index_list.append(i)
    return valleys_index_list

print(f'Valleys: {valleys(data)}')

# define function peaks_and_valleys
# -uses the above two functions to compile a single list of the peaks and valleys 
# -in order of appearance in the original data.
def peaks_and_valleys():
    peaks_and_valleys_list = peaks(data) + valleys(data)
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list

print(f'Peaks and Valleys: {peaks_and_valleys()}')

#---------------------------------------------------------------------------------------
# Optional Version 2 - Using the data draw the image of x's

# data = [1,2,3,4,3,2,3,4,5,6,7,6,5,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,6,7,8,9,8]
max_data = max(data)
new_list = []
i = max_data
while i > 0:
    variable_concatenation = ''
    for num in data:
        if num >= i and len(str(num)) == 1:
            variable_concatenation += (' x ')
        elif num >= i and len(str(num)) == 2: #formatting for double digit number in list
            variable_concatenation += ('  x ')
        elif len(str(num)) == 1:
            variable_concatenation += ('   ') 
        elif len(str(num)) == 2:    # formatting for double digit number in list
            variable_concatenation += ('    ')            
    i -= 1
    print(variable_concatenation)
print(data)

#--------------------------------------------------------------------------------------------
# Optional Version 3 - add o's in the valleys to the hight of lowest peak between the valleys
