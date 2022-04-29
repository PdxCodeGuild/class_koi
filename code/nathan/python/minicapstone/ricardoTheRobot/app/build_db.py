def import_challenges():
    challenges_list = []
    with open('challenges.txt', 'r') as f:
        holder_list = []
        contents = f.read()

        contents = contents.split('\n')
        for i in contents:
            holder_list.append(i)
        for i in holder_list:
            temp_list = []
            section = i.split(' ', 1)
            name = section[1].split(': ', 1)
            description = name[1]
            temp_list.append(section[0])
            temp_list.append(name[0])
            temp_list.append(description)
            challenges_list.append(temp_list)
    return challenges_list

# topic_list = {
#     '1': 'Arrays and Strings',
#     '2': 'Linked Lists',
#     '3': 'Stacks and Queues',
#     '4': 'Trees and Graphs',
#     '5': 'Bit Manipulation',
#     '6': 'Math and Logic Puzzles',
#     '7': 'Object-Oriented Design',
#     '8': 'Recursion and Dynamic Programming',
# }