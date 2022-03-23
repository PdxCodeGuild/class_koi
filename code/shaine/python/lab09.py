#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 9: Peaks and Valleys
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []

    for i in range(1, len(data)-1):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peaks.append(data[i])

    return peaks


def valleys(data):
    valleys = []

    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            valleys.append(data[i])

    return valleys

total_peaks = peaks(data)

total_valleys = valleys(data)

peaks_and_valleys = peaks(data) + valleys(data)

print(f'Peaks {total_peaks}')

print(f'Valleys {total_valleys}')

print(f'Peaks an Valleys {peaks_and_valleys}')

