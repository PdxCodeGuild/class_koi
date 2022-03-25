data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

def peaks(data):

    peak_list = []
   
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            pass
        else:
            if data[i] > data[i-1] and data[i] > data[i+1]:
                peak_list.append(i)
    return peak_list

def valleys(data):

    valleys_list = []

    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            pass
        else:
            if data[i] < data[i-1] and data[i] < data[i+1]:
                valleys_list.append(i)
    return valleys_list

peaks_data = peaks(data)
valleys_data = valleys(data)

def peaks_and_valleys(peaks_data,valleys_data):

    peaks_data.extend(valleys_data)
    return sorted(peaks_data)

peaks_x_valleys = peaks_and_valleys(peaks_data,valleys_data)

print("\nWelcome to Topography Highs and Lows!")
print(f'\n1. Peaks: {peaks_data}')
print(f'\n2. Valleys: {valleys_data}')
print(f'\n3. Peaks and Valleys: {peaks_x_valleys}\n')
