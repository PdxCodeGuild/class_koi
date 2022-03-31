'''
Lab 9: Peaks and Valleys

-version 2: print the x's on top of the values 
    loop through the list, range(range of values in list)
    if (max value in list - loop number) >= value at index location, print an x
    else print a space

-version 3: print 0's in the valleys
    similar to loop above
    only open the loop if peak has been reached
        print 0's
    close loop when a value equaling the peak is reached
    

'''

#
#                                                 X  0  0  0  0  0  X
#                                              X  X  X  0  0  0  X  X
#                         X  0  0  0  0  0  X  X  X  X  X  0  X  X  X
#                      X  X  X  0  0  0  X  X  X  X  X  X  X  X  X  X
#                   X  X  X  X  X  0  X  X  X  X  X  X  X  X  X  X  X
#                X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#          X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_valleys_list = []

# peaks
def peaks():
    for num in range(len(data) - 1):
        if data[num - 1] < data[num] and data[num + 1] < data [num] and num != 0 and num != len(data):
            peaks_valleys_list.append(num)

# valleys
def valleys():
    for num in range(len(data) - 1):
        if data[num - 1] > data[num] and data[num + 1] > data [num] and num != 0 and num != len(data):
            peaks_valleys_list.append(num)

# peaks_and_valleys
def peaks_and_valleys():
    peaks()
    valleys()
    peaks_valleys_list.sort()
    print(peaks_valleys_list)

peaks_and_valleys()
