# Lab 9: Peaks and Valleys
# Version 1
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
    """Uses the functions peaks() and valleys() to compile a single list of the peaks and valleys in order of appearance in the original data."""
    
    dict_of_peak_indecies = peaks(data)
    dict_of_valley_indices = valleys(data)
    dict_of_peaks_and_valleys_indecies = dict_of_peak_indecies | dict_of_valley_indices
    list_of_peaks_and_valleys_indecies = []
    
    for index, _ in enumerate(data):
        if index in dict_of_peaks_and_valleys_indecies:
            input_data = index, dict_of_peaks_and_valleys_indecies[index]
            list_of_peaks_and_valleys_indecies.append(input_data)
    

            
    print(f"\nFor the dataset of heights: {data}:")
    return(f"Peaks and valleys can be found at these list index/indices: {list_of_peaks_and_valleys_indecies}")




print(peaks_and_valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))




