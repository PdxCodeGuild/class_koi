# Lab 9: Peaks and Valleys
# Version 2
# Mitch Chapman

def peaks(data):
    """Returns the indices of peaks. A peak has a lower number on both the left and the right."""
    peaks = {}

    for indx, num in enumerate(data):
        
        if indx == 0:
            pass
        elif indx == len(data) - 1:
            pass
        else:
            if data[indx - 1] < num > data[indx + 1]:
                peaks[indx] = 'peak'
    return peaks
    

def valleys(data):
    """Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right."""
    valleys = {}
    
    for indx, num in enumerate(data):
        if indx == 0:
            pass
        elif indx == len(data) - 1:
            pass
        else:
            if data[indx - 1] > num < data[indx + 1]:
                valleys[indx] = 'valley'
    return valleys
    
    
def peaks_and_valleys(data:list):
    """
    Uses the functions peaks() and valleys() to compile a single list of the peaks and valleys in order of appearance in the original data. 
    Also prints 'x' above each number in the terminal for a visualization of the peaks and valleys.
    """
    
    dict_of_peak_indecies = peaks(data)
    dict_of_valley_indices = valleys(data)
    dict_of_peaks_and_valleys_indecies = dict_of_peak_indecies | dict_of_valley_indices
    list_of_peaks_and_valleys_indecies = []
    
    height = max(data)
    x_matrix = {}
    
    
    for i in range(1, height+1):
        x_matrix[i] = []
    
    
    for index, _ in enumerate(data):
        if index in dict_of_peaks_and_valleys_indecies:
            input_data = index, dict_of_peaks_and_valleys_indecies[index]
            list_of_peaks_and_valleys_indecies.append(input_data)

    for key in reversed(x_matrix.keys()):
        for index, num in enumerate(data):
            if num == key or num > key:
                x_matrix[key].append(index)

    for key in reversed(x_matrix.keys()):
        temp_list = []
        for index, _ in enumerate(data):
            if index in x_matrix[key]:
                temp_list.append("x")
            else:
                temp_list.append(" ")
        print("                             " + "  ".join(temp_list))
        
            
     
    print(f"For the dataset of heights: {data}:")
    return(f"Peaks and valleys can be found at these list index/indices: {list_of_peaks_and_valleys_indecies}")




print(peaks_and_valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))




