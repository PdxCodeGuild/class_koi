# You may get a FileNotFoundError: FileNotFoundError: [Errno 2] No such file or directory: 'data/fire-and-ice.txt'
# Make sure that the filepath is relative to where you are running the script
# path_to_data_folder = 'users/pete/code-guild/class_koi/code/pete/python/examples/data/' # absolute path
path_to_data_folder = 'code/pete/python/examples/data/' # relative path

def read_text_file(filename):
    # if you have problems reading the text, give open the keyword argument encoding='utf-8'
    with open(path_to_data_folder + filename, 'r', encoding='utf-8') as f:
        # f, or file, is an object that can read and write to files
        # print(f) # <_io.TextIOWrapper name='code/pete/python/examples/data/fire-and-ice.txt' mode='r' encoding='UTF-8'>
        contents = f.read()
    return contents

# print(read_text_file('fire-and-ice.txt'))

def poem_improver(filename, filename2):
    # contents = read_text_file(filename)
    lines = read_text_file(filename).split('\n')
    # print(lines)
    new_lines = []
    for line in lines: # under the hoood, it runs: line = lines[i]
        # capitalize ever letter
        line = line.upper() # this redefines the variable line, but does not affect the list
        # have every line end with an exclamation point: !
        if line[-1] == '.' or line[-1] == ',': # if line[-1] in '.,':
            line = line[:-1]
            # print(line)

        line = line + '!'
        new_lines.append(line)
    # print(lines)
    # print(new_lines)

    improved_poem = '\n'.join(new_lines)
    # print(improved_poem)

    with open(path_to_data_folder + filename2, 'w') as f:
        f.write(improved_poem)

poem_improver('fire-and-ice.txt', 'FIRE-AND-ICE-IMPROVED.TXT')


# when getting lines of a text file, here are 2 ways
# lines = f.readlines() # this one preserves the '\n' newline character in each string in the list
# lines = f.read().split('\n') # this one splits on the '\n' newline character, removing all from the strings
