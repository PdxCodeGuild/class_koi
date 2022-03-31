'''
PDX Code Guild - Class Koi
Lab 09 - Peaks and Valleys
Matt Walsh
'''

 
# Version 1
""" 
def peaks(input):
    # create empty list to hold peak indices
    peak_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is higher than its neighbors, add its index to peak_index
        elif input[x - 1] < input[x] and input[x + 1] < input[x]:
            peak_index.append(x)
    # sort and return peak_index
    peak_index.sort()
    return peak_index

def valleys(input):
    # create empty list to hold valey indices
    valley_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is lower than its neighbors, add its index to valley_index
        elif input[x - 1] > input[x] and input[x + 1] > input[x]:
            valley_index.append(x)
    # sort and return valley_index
    valley_index.sort()
    return valley_index

def peaks_and_valleys(input):
    # call peaks and valleys functions and combine into 1 list
    combined = peaks(input) + valleys(input)
    # sort and return results
    combined.sort()
    return combined

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# display results of each function
print(f'Peaks:\n{peaks(data)}')
print(f'Valleys:\n{valleys(data)}')
print(f'Combined:\n{peaks_and_valleys(data)}')
"""


# Version 2
""" 
def peaks(input):
    # create empty list to hold peak indices
    peak_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is higher than its neighbors, add its index to peak_index
        elif input[x - 1] < input[x] and input[x + 1] < input[x]:
            peak_index.append(x)
    # sort and return peak_index
    peak_index.sort()
    return peak_index

def valleys(input):
    # create empty list to hold valey indices
    valley_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is lower than its neighbors, add its index to valley_index
        elif input[x - 1] > input[x] and input[x + 1] > input[x]:
            valley_index.append(x)
    # sort and return valley_index
    valley_index.sort()
    return valley_index

def peaks_and_valleys(input):
    # call peaks and valleys functions and combine into 1 list
    combined = peaks(input) + valleys(input)
    # sort and return results
    combined.sort()
    return combined

def graph_gen(input):
    # determine lowest and highest values in dataset
    low = input[0]
    high = 0
    for x in range(len(input)):
        if input[x] < low:
            low = input[x]
        elif input[x] > high:
            high = input[x]
    # generate graph dictionary with keys
    graph = {}
    for x in range(low, high + 1):\
        graph[x] = []
    # iterate through graph rows
    for row in graph:
        # iterate through digits in each row
        for digit in input:
            # append an 'X' if the value is greater than or equal to row value
            if digit >= row:
                graph[row].append('X')
            # append a ' ' if the value is less than row value
            else:
                graph[row].append(' ')
        graph[row] = ' '.join(graph[row])
    # generate multiline string from graph dictionary
    graph_str =''
    i = high
    # add each row except with new line
    while i > low:
        graph_str += graph[i] + '\n'
        i -= 1
    # add last row
    graph_str += graph[i]


    return graph_str

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# make string from data to display below graph
data_str =''
for x in data:
    data_str += str(x)

# display graph above data string
print(graph_gen(data))
print(' '.join(data_str))
"""


# Version 3

def peaks(input):
    # create empty list to hold peak indices
    peak_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is higher than its neighbors, add its index to peak_index
        elif input[x - 1] < input[x] and input[x + 1] < input[x]:
            peak_index.append(x)
    # sort and return peak_index
    peak_index.sort()
    return peak_index

def valleys(input):
    # create empty list to hold valey indices
    valley_index = []
    # iterate through each item in the list
    for x in range(len(input)):
        # ignore the first and last digits
        if x == 0 or x == len(input) - 1:
            continue
        # if digit is lower than its neighbors, add its index to valley_index
        elif input[x - 1] > input[x] and input[x + 1] > input[x]:
            valley_index.append(x)
    # sort and return valley_index
    valley_index.sort()
    return valley_index

def peaks_and_valleys(input):
    # call peaks and valleys functions and combine into 1 list
    combined = peaks(input) + valleys(input)
    # sort and return results
    combined.sort()
    return combined

def graph_gen(input):
    # determine lowest and highest values in dataset
    low = input[0]
    high = 0
    for x in range(len(input)):
        if input[x] < low:
            low = input[x]
        elif input[x] > high:
            high = input[x]
    # generate graph dictionary with keys
    graph = {}
    for x in range(low, high + 1):\
        graph[x] = []
    # variable to count water added later
    water = 0
    # iterate through graph rows
    for row in graph:
        # iterate through digits in each row
        for digit in input:
            # append an 'X' if the value is greater than or equal to row value
            if digit >= row:
                graph[row].append('X')
            # append a ' ' if the value is less than row value
            else:
                graph[row].append(' ')
        # iterate through columns in graph and add water ('O') where needed
        for x in range(len(graph[row])):
            # ignore current 'X' locations
            if graph[row][x] == 'X':
                continue
            # if there is an 'X' to the left and right, change to 'O'
            elif 'X' in graph[row][:x] and 'X' in graph[row][x + 1:]:
                graph[row][x] = 'O'
                water += 1
        graph[row] = ' '.join(graph[row])
    # generate multiline string from graph dictionary
    graph_str =''
    i = high
    # add each row except with new line
    while i > low:
        graph_str += graph[i] + '\n'
        i -= 1
    # add last row
    graph_str += graph[i]


    return graph_str, water

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# make string from data to display below graph
data_str =''
for x in data:
    data_str += str(x)

# display water collected and graph above data string
print(graph_gen(data)[0])
print(' '.join(data_str))
print(f'\n{graph_gen(data)[1]} water collected.')