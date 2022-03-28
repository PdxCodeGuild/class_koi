# Lab 09, Peaks and Valleys ---- #

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

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


def peaks_and_valleys(data):
    p = peaks(data) # variable equaling function
    v = valleys(data)
    peaks_valleys = p + v
    peaks_valleys.sort()
    
    return peaks_valleys
    

print(peaks_and_valleys(data))