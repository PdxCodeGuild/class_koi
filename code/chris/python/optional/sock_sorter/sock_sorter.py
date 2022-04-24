'''
Optional Lab: Sock Sorter
'''

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

sock_collection = []

sock_dict = {
    'ankle': 0,
    'crew': 0,
    'calf': 0,
    'thigh': 0,
}

sock_count = 0

while len(sock_collection) < 100:
    sock_collection.append(random.choice(sock_types))

sock_collection.sort()

for sock in sock_collection:
    sock_dict[sock] += 1

for sock in sock_dict:
    loner = sock_dict[sock] % 2
    if loner == 0:
        pairs = int(sock_dict[sock] / 2)
        print(f'{pairs} pairs of {sock}')
    elif loner == 1:
        pairs = sock_dict[sock] // 2
        print(f'{pairs} pairs of {sock}, and {loner} loner.')