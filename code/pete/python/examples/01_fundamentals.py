# """Variables"""

# # x = 5
# # print(id(x))
# # message = 'goodbye'
# # print(id(message))

# """Objects & Types"""
# # do type checks on your variables
# print(type('hello'))
# print(type('goodbye'))

# print(type(None))

# print(type(True))

# def add(x, y):
#     return x + y

# print(type(add))

# message1 = 'hello' # this is a literal because it's defined in the source code
# print(message1.upper()) # .upper() is a string method
# # every type is going to have its own methods and attributes

# message2 = input('give me message 2: ') # message2 is not a literal, it's defined outside of the source code

# numbers = [1, 2, 3, 4, 5]

# """
# Type Conversion
# """
# int_11 = int('11')
# print(int_11)
# print(type(int_11))

# str_11 = str('11')
# print(str_11)
# print(type(str_11))

"""Mutability"""
# strings, ints, tuples, and other types are immutable
# they cannot be changed, they can only be redefined
x = 13
print(x, id(x))

x += 5 # shorthand for x = x + 5
print(x, id(x))

message = 'hello'
message += ' world' # message = 'hello' + ' world'

# list, dictionaries, and other types are mutable
# they are dynamic objects whose properties can change

colors = ['red', 'green', 'blue']
print(colors, id(colors))

colors.append('yellow') # the list is changed but is still the same list
print(colors, id(colors))

"""Print Stuff"""

print(1, end='')
print(2, end='')
print(3, end='')
print(4, end='')
print(5, end='')
print(6, end='')
print(7)

print(1, 2, 3, 4, 5, sep='   ')


"""time.sleep"""
import time

print("Why is Python on land?")
time.sleep(2)
print("Because it's above C level.")