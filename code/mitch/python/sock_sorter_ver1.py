# Sock Sorter
# Version 1
# Mitch Chapman

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = []

for _ in range(100):
    socks.append(random.choice(sock_types))

for sock_type in sock_types:
    if (socks.count(sock_type) % 2) == 0:
        print(f"{sock_type} sock pairs: {int(socks.count(sock_type) / 2)}")
    else:
        print(f"{sock_type} sock pairs: {socks.count(sock_type) // 2}")
        print(f"  ... and a lone {sock_type} sock was found.")
























