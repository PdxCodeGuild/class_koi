"""Booleans"""
# and
# and is used to chain booleans together
# a chain of booleans will evauluate to True if all are True
# it will evaluate to False if one is False
print(True and True)
print(True and True and False)

print(1 < 2 and 2 == 2)
print(1 < 2 and 2 == 2 and 2 + 2 == 5)

message = input('enter something lowercase and shorter than 10 characters: ')
valid = message.islower() and len(message) < 10
if valid:
    print(f'"{message}" is valid')
else:
    print(f'"{message}" is invalid')

# or
# or is used to chain booleans together
# that chain of boolenas will evaluate to True if one is True
# it will evaluate to False if all are False

print(False or False)
print(False or True)
print(False or False or False or False or False or False or False or False or False or False or False or True)

# not

print(not True)
print(not False)

print(1 not in [1, 2, 3])

plant = {'colors': 'red and green', 'name': 'red nerve plant'}
colors = plant.get('colors')
if colors is not None: # !=
    print('the colors are ' + colors)
else:
    print('no colors info')


soil = plant.get('soil')
if soil is not None:
    print('the soil is ' + soil)
else:
    print('no soil info')

player_ones_turn = True
while True:
    if player_ones_turn:
        print('player one, your turn...')
    else:
        print('player two, your turn')
    go_again = input('go again? (y/n) ')
    if go_again == 'y':
        player_ones_turn = not player_ones_turn
    else:
        break

"""Comparisons"""

print(1 == 1 == 1)
print(1 == 1 and 1 == 1)

x = 7

print(5 < x < 6)
print(5 < x < 6 or 0 < x < 10)

# in
colors = ['red', 'green', 'blue']
print('green' in colors)

for color in colors:
    print('r' in color)

print('ete' in 'pete')

# is

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] is [1, 2, 3])

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)

print(list1 is list3)

print(id(list1))
print(id(list2))
print(id(list3))

"""Short Circuited Evaluation"""
print(True and True and False and True and True and True)
#                       ^   ^
# as soon as the first False is hit, it knows the whole thing is false

print(False or False or False or True or False or True)
#                                ^  ^
# as soon as the first True is hit, it knows the whole thing is True

"""Shorthand"""
def min(a, b):
    # if a < b:
    #     return a
    # else:
    #     return b
    return a if a < b else b
print(min(5, 2)) # 2


"""Truthy and Falsey"""
if 1:
    print('one is truthy')

if 'hello':
    print("'hello' is truthy")

if 0:
    print('0 is truthy')

if '':
    print('an empty string is truthy')

if []:
    print('this wont show')


# other use for or

username = input('Please enter your username (leave blank for \'anonymous\'): ')
username = username or 'anonymous'

print('your username is: ' + username)