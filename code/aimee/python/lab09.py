# Lab 09, Peaks and Valleys ---- #

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# indices 0 - 20 

# def peaks(data): # return the index position of number with lower value on either side
#     #peak_total = []
#     for index, elem in enumerate(data):
#         if data[index+1] < elem and data[index-1] < elem:
#             # peak_total.append(index)
#             return index
#     return index # is returning index 6, should be 6 and 14
#         # else:
#         #     break # gives none

# # def valleys():
# #     return True 

#print(peaks(data)) # list index is out of range

def peaks(data):
    peak_total = []
    for i in range(len(data)): # i is in the range/length of data
        if i != 0 and i != (len(data) -1): # i isn't zero, i isn't less than the length of data
            if data[i-1] < data[i] and data[i+1] < data[i]: # if i is less than number before and after
                peak_total.append(i) # add i to the list if it meets above conditions
        
    return peak_total

def valleys(data):
    valley_total = []
    for i in range(len(data)): 
        if i != 0 and i != (len(data) -1): 
            if data[i-1] > data[i] and data[i+1] > data[i]: 
                valley_total.append(i) 
        
    return valley_total

# print(peaks(data)) #[6, 14]
# print(valleys(data)) #[9, 17]


def peaks_and_valleys(data):
    # peaks_valleys = []
    p = peaks(data) # variable equaling function
    v = valleys(data)
    peaks_valleys = p + v
    peaks_valleys.sort()
    
    return peaks_valleys
    

print(peaks_and_valleys(data))