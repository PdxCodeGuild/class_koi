'''
PDX Code Guild - Class Koi
Optional Lab - Sock Sorter
Matt Walsh
'''

 
# Version 1
'''
# import choice for sock creation
from random import choice

# dictionary to hold sock types and their count
socks = {
    'ankle':0,
    'crew':0,
    'calf':0,
    'thigh':0,
}

def sock_creator(num):
    """
    Create number of socks input as parameter
    """
    # randomly generate socks and increment their count in dictionary
    for i in range(num):
        socks[choice(list(socks.keys()))] += 1
    pass

def sock_counter(socks):
    """
    Count sock pairs and loaners in dictionary
    """
    # iterate through sock types
    for sock in socks.keys():
        # use floor division and modulus to find pairs and loners
        pairs = socks[sock] // 2
        loners = socks[sock] % 2
        # display results
        print(f'{pairs} pairs of {sock} socks and {loners} {"loner" if loners == 1 else "loners"}')
    pass

# number of socks to create and count
num_socks = 100

# create socks out of thin air
sock_creator(num_socks)

# display results
print('You have:')
sock_count = sock_counter(socks)
'''


# Version 2

# import choice for sock creation
from random import choice

# lists of sock types and colors
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']

# list to hold each sock in tuple
socks = []

def sock_creator(num):
    """
    Create number of socks input as parameter
    """
    # randomly generate socks as tuples
    for i in range(num):
        socks.append((choice(sock_colors),choice(sock_types)))
    pass

def sock_counter(socks):
    """
    Count sock pairs and loaners in dictionary
    """
    # get list of unique sock types and sort
    unique = list(set(socks))
    unique.sort()
    # iterate through unique sock types
    for sock in unique:
        # use floor division and modulus to find pairs and loners
        pairs = socks.count(sock) // 2
        loners = socks.count(sock) % 2
        # display results
        print(f'{pairs} pairs of {" ".join(sock)} socks and {loners} {"loner" if loners == 1 else "loners"}')
    pass

# number of socks to create and count
num_socks = 100

# create socks out of thin air
sock_creator(num_socks)

# display results
print('You have:')
sock_count = sock_counter(socks)