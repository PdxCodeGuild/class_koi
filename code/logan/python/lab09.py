data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(input):
    peaks = []
    for i in range(len(input)):
        if i != 0 and i != -1:
            if input[i] > input[i - 1] and input[i] > input[i + 1]:
                peaks.append(input[i])
    return peaks

# print(range(len(data)))
# print(peaks(data))
print(len(data))
