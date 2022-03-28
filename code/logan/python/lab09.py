##Lab09V1
##Code

## Uncomment data if you want to pass the data set as a test.
## There are helpful print statements for testing as the
## bottom of the page
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# def peaks(input):
# # Pulls out the peaks in a list, inputs them in a list
#     peak_indices = []
#     for i in range(len(input)):
#         if i != 0 and i != (len(input) -1):
#             if input[i] > input[i - 1] and input[i] > input[i + 1]:
#                 peak_indices.append(i)
#     return peak_indices

# def valleys(input):
# # Pulls out the valleys in a list, outputs them in a list
#     valley_indices = []
#     for i in range(len(input)):
#         if i != 0 and i != (len(input) -1):
#             if input[i] < input[i - 1] and input[i] < input[i + 1]:
#                 valley_indices.append(i)
#     return valley_indices

# def peaks_and_valleys(input):
# # Outputs a list of all peaks and valleys in a list in the order they appear in the input
#     output = []
#     for valley in valleys(input):
#         output.append(valley)
#     for peak in peaks(input):
#         output.append(peak)
#     output.sort()
#     return output

# ## Tests
# # print(peaks(data))
# # print(valleys(data))
# # print(peaks_and_valleys(data))

#####
##Version 2
##Code

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def line_printer(input):
# Draws peaks and valleys with Xs
    print("")
    art = []
    for value in range(0, max(input)):
        string = ""
        for item in input:
            if item > value:
                string += "X"
            else:
                string += " "
        art.append(string)
    art.reverse()
    for line in art:
        print(line)
    second_string = ""
    for int in input:
        second_string += str(int)
    print(second_string)
    print("")

line_printer(data)
