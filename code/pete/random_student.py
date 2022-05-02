# import random # import the entire random module

from random import randint, choice, shuffle, choices # import only what you need from the random module

# Version 1: print out a random student name

students = [
   'adam',
   'aimee',
   'brandon',
   'chris',
   'dan',
   'logan',
   'matt',
   'mitch',
   'moss',
   'nathan',
   'shaine',
]

# print(students[randint(0, len(students) - 1)])
# print(choice(students))


def create_groups(students, num_of_groups):
    """Given a list of student names, and a number of groups,
    divies up the students into that number of lists
    and returns a list of those lists"""
    shuffle(students)
    groups = []

    while len(students):
        this_group = []
        group_size = len(students) // num_of_groups
        for i in range(group_size):
            this_group.append(students.pop(0))
        num_of_groups -= 1
        groups.append(this_group)
    
    return groups

    # for i in range(num_of_groups):
    #     group = []

    #     # step 2: ???

    #     groups.append(group)

    # print(len(students) % num_of_groups)

create_groups(students, 3)