# Version 1

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_and_vallleys = []

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):
    
    for i in range(len(data)):   
        if i >= 1 and i <= 19 and data[i] > data[i+1] and data[i] > data[i-1]:
            print('peak')
            print(data[i])
            print(data[i-1], data[i+1])
            if True:
                peaks_and_vallleys.append(i)
        
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
def valleys(data):
    for i in range(len(data)):
        
        if i >= 1 and i <= 19 and data[i] < data[i+1] and data[i] < data[i-1]:
            print('valley')
            print(data[i])
            print(data[i-1], data[i+1])
            if True:
                peaks_and_vallleys.append(i)

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
def peaks_and_valleys():
    for i in range(len(data)):   
        if i >= 1 and i <= 19 and data[i] > data[i+1] and data[i] > data[i-1]:
            print('peak')
            print(data[i])
            print(data[i-1], data[i+1])
            continue
       
        if i >= 1 and i <= 19 and data[i] < data[i+1] and data[i] < data[i-1]:
            if True:
                peaks_and_vallleys.append(i)
            print('valley')
            print(data[i])
            print(data[i-1], data[i+1])
            continue
print('PEAKS-------------')
peaks(data)
print('Valleys ---------------')
valleys(data)
print('Peaks and Valleys ---------')
peaks_and_valleys()