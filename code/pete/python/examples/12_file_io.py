# You may get a FileNotFoundError: FileNotFoundError: [Errno 2] No such file or directory: 'data/fire-and-ice.txt'
# Make sure that the filepath is relative to where you are running the script
# path_to_data_folder = 'users/pete/code-guild/class_koi/code/pete/python/examples/data/' # absolute path
path_to_data_folder = 'code/pete/python/examples/data/' # relative path

# if you have problems reading the text, give open the keyword argument encoding='utf-8'
with open(path_to_data_folder + 'fire-and-ice.txt', 'r', encoding='utf-8') as f:
    # f, or file, is an object that can read and write to files
    print(f) # <_io.TextIOWrapper name='code/pete/python/examples/data/fire-and-ice.txt' mode='r' encoding='UTF-8'>
    # print(f.read())
    contents = f.read()
    # lines = f.readlines()
    # lines = f.read().split('\n') # usually better for getting lines in a list

print(contents)
# print(lines)