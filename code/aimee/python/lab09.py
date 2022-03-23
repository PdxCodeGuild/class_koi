# Lab 09, Peaks and Valleys ---- #

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# indices 0 - 20 

def peaks(data): # return the index position of number with lower value on either side
    peak_total = []
    for index, elem in enumerate(data):
        if data[index+1] < elem and data[index-1] < elem:
            peak_total.append(index)
    return peak_total # is returning index 6, should be 6 and 14
        # else:
        #     break # gives none

# def valleys():
#     return True 

print(peaks(data))
