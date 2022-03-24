# arguments & parameters


def print_things(parameter1, parameter2): # parameters are what you call var passed to function inside its definition
    """
    takes in 2 strings and prints them
    """
    print(parameter1 + ' ' + parameter2)

print_things('thing1', 'thing2') # arguments are what you actually pass to the function

argument1 = 'thing3'
argument2 = 'thing4'
print_things(argument1, argument2)

# optional arguments
def staff_info(first_name, last_name, role='Teacher'):
    return f'{first_name} {last_name} is a {role}.'

pete_info = staff_info('Pete', 'Jones')
lisa_info = staff_info('Lisa', 'Brown', 'TA')
print(pete_info, lisa_info)


# keyword arguments
def staff_info_v2(first_name='unknown', last_name='unknown', role='unknown'):
    return f'{first_name} {last_name} is a {role}.'

mysterious_stranger_info = staff_info_v2()
print(mysterious_stranger_info)

slightly_less_mysterious_stranger_info = staff_info_v2(role='TA', first_name='steve')
print(slightly_less_mysterious_stranger_info)

slightly_less_mysterious_stranger2_info = staff_info_v2('sheri', role='director')
print(slightly_less_mysterious_stranger2_info)

"""
EXERCISE 1
Write an add function that returns the sum of two numbers
"""


def add(x, y):
    """
    given numbers, x and y, returns their sum
    """
    return x + y


print(add(1, 2))  # 3
print(add(3, 7))  # 10

"""
EXERCISE 2
Write a function that capitalizes the first letter of every word in a string
"""


def capitalize(message: str):
    """
    given a string message, returns a version of that message
    with every word capitalized
    """
    return message.title()


print(capitalize('capitalize this message'))  # Capitalize This Message


"""
EXERCISE 3
Write an add function that takes in *args and returns the sum of all numbers
"""


def add_plus(*nums):
    """given nums, returns the sum of all those numbers"""
    print(nums)
    print(*nums)
    return sum(nums)


print(add_plus(1, 2, 3, 4, 5, 6))  # 21


def print_things(*args):
    print(type(args))
    print(args)
    for arg in args:
        print(arg)

print_things(1, 2, 3)

# print takes in *values (an example of *args)
print(1, 2, 3, 4, 5)


"""returns"""


def weather_report(temperature): # return ends the function, the remaining lines won't run
    """from a given temperature (int) returns a string describing the weather"""
    if temperature < 60:
        return 'cold'
    if temperature < 70:
        return 'warm'
    if temperature < 80:
        return 'pretty warm'
    if temperature < 90:
        return 'hot'
    return "wow it's so hot!"

def weather_report_if_elif_else(temperature): # this version uses one return with an if/elif/else chain
    if temperature < 60:
        report = 'cold'
    elif temperature < 70:
        report = 'warm'
    elif temperature < 80:
        report = 'pretty warm'
    elif temperature < 90:
        report = 'hot'
    else:
        report = "wow it's so hot!"
    return report

portland_weather = weather_report(43)
print(portland_weather)

report = weather_report_if_elif_else(43)
print(report)

# while True:
#     temp = int(input('gimme a temperature: '))
#     print(weather_report(temp))

temperatures = [55, 65, 75, 85, 95]

# for temp in temperatures:
# 	print(temp, weather_report(temp))

"""Implicit Return"""
# if a function doesn't have a return, or if the return line never executes,
# the function will return None by default

def gimme_none():
    print('this returns nothing!!')

none = gimme_none()
print(none)

"""multiple return values"""
def get_dimensions():
    return 500, 200

# tuple unpacking
width, height = get_dimensions()
print(width)
print(height)

dimensions = get_dimensions()
print(dimensions)
print(dimensions[0], dimensions[1])

width, height = (500, 200)
print(width, height)

"""recursion"""
def crash_python(i=0):
    print(i)
    i += 1
    crash_python(i)
# crash_python()


def for_loop(i, sequence):
    print(sequence[i])
    i += 1
    if i == len(sequence):
        return
    for_loop(i, sequence)


colors = ['red', 'green', 'blue']
for_loop(0, colors)

"""lambda"""

subtract = lambda x, y: x - y
print(subtract(1,5))

def subtract(x, y):
    return x - y


def multiply1(x, y): # a pure function can take in 0 or more parameters and returns a value
    return x * y

def multiply2(x, y): # this function has side effects, it prints something out
    print(x * y)


result = multiply1(2, 3)
# print(result, 'is the product of  2 and 3')

# print(multiply1(2, 2))

# multiply2(4, 5)