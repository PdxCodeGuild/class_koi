# Sock Sorter
# Version 2
# Mitch Chapman

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
socks = []

for _ in range(100):
    sock = (random.choice(sock_colors), random.choice(sock_types))
    socks.append(sock)


for type in sock_types:
    for color in sock_colors:
        argument = color, type
        if socks.count(argument) % 2 == 0:
            print(f"{color.title()} {type} sock pairs: {int(socks.count(argument) / 2)}")
        else:
            print(f"{color.title()} {type} sock pairs: {socks.count(argument) // 2}")
            print(f"  ... and a lone {color} {type} sock was found.")
























