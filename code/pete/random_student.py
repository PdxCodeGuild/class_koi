# import random # import the entire random module

from random import randint, choice # import only what you need from the random module

# Version 1: print out a random student name

students = [
    'adam',
    'aimee',
    'brandon',
    'chris',
    'dan',
    'logan',
    'lujock',
    'matt',
    'mitch',
    'moss',
    'nathan',
    'shaine',
]

print(students[randint(0, len(students))])
# print(choice(students))