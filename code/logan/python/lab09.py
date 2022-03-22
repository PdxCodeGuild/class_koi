data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(input):
    peak_indices = []
    for i in range(len(input)):
        if i != 0 and i != (len(input) -1):
            if input[i] > input[i - 1] and input[i] > input[i + 1]:
                peak_indices.append(i)
    return peak_indices

def valleys(input):
    valley_indices = []


## Tests

# print(len(data))
# print(range(len(data)))

# for item in range(len(data)):
#     print(item)
# print(peaks(data))
# print(len(data))
