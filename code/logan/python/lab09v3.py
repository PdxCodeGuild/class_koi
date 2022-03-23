# art = ["XX X ", " X XX"]

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

data_as_string = ""
for item in data:
    data_as_string += str(item)

def line_saver(input):
# returns set of lines that would have been printed by line printer
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
    counter = 0
    for level in rainy_art:
        for character in level:
            if character == "O":
                counter += 1
    return counter



mountains = line_saver(data)
rainy_mountains = rainfall(mountains)

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