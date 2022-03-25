## Lab09 V3
## Code

# art = ["XX X ", " X XX"]

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# This just turns the data into a string.
data_as_string = ""
for item in data:
    data_as_string += str(item)

def line_saver(input):
#"""
# Converts list of data into a list of strings that can be 
# later 'stacked' on each other to visualize the data.
# """
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
    return art

def rainfall(input_art):
#"""
# This 'pours water' on the mountains in the appropriate places,
# allowing it to be visualized and counted later.
#
#
# Really what it does is output a new list of stackable strings that
# have Os everywhere water would come to rest in our visual 
# model.
# """
    art_after_rain = []
    for line in input_art:
        string_after_rain = ""
        pools = []
        for char_index in range(0, len(line)):
            if line[char_index] == "X" and char_index != (len(line) - 1):
                if line[char_index + 1] == " ":
                    pool_search = True
                    # Testing loop...
                    while pool_search == True:
                        for ii_char_index in range(char_index + 1, len(line)):
                            if line[ii_char_index] == "X":
                                pools.append((char_index, ii_char_index))
                                pool_search = False
                                break
                            elif line[ii_char_index] != "X" and ii_char_index == (len(line) - 1):
                                pool_search = False
                                break
        # Pool finder seems to work...on to this section
        for char_index in range(0, len(line)):
            wet = False
            if line[char_index] == " ":
                for pool in pools:
                    if char_index in range(pool[0], pool[1]):
                        # string_after_rain += "O"
                        wet = True
                        break

                if wet == True:
                    string_after_rain += "O"
                    wet = False
                else:
                    string_after_rain += " "
            else:
                string_after_rain += "X"
        art_after_rain.append(string_after_rain)
    return art_after_rain

def total_rainfall(rainy_art):
#"""
# This just counts the Os across all strings in the list 
# spit out by the rainfall function,
# which will give the total amount of rainfall.
#"""
    counter = 0
    for level in rainy_art:
        for character in level:
            if character == "O":
                counter += 1
    return counter

# generates some data using functions
mountains = line_saver(data)
rainy_mountains = rainfall(mountains)

# output

print("""
Mountains...
""")
for line in mountains:
    print(line)
print(data_as_string)

print("""
Mountains after rainfall...
""")

for line in rainy_mountains:
    print(line)
print(data_as_string)

print(f"""
Total rainfall is {total_rainfall(rainy_mountains)} units.
""")