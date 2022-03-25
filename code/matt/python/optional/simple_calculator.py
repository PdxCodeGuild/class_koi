'''
PDX Code Guild - Class Koi
Optional Lab - Simple Calculator
Matt Walsh
'''

 
# Version 1
'''
def int_or_flt(input):
    """
    Converts to integer if whole number, otherwise returns float
    Also tries to eliminate floating point errors
    """
    # split input for floating point error detection
    x = str(input).split('.')
    # if whole number, return an int
    if float(input) % 1 == 0:
        return int(input)
    # if floating point error detected, use round to correct
    elif '9999' in x[1]:
        return round(float(input),(x[1].find('9999')))
    # otherwise, return a float
    else:
        return float(input)


def maths(x,y,operator):
    """
    Performs basic arithmatic based on input operator
    """
    # perform and return maths
    if operator == '+':
        return int_or_flt(x + y)
    elif operator == '-':
        return int_or_flt(x - y)
    elif operator == '*':
        return int_or_flt(x * y)
    elif operator == '/':
        return int_or_flt(x / y)

# list of operators for validation
operators = ['+','-','*','/']

while True:
    # loop to accept and validate operator input
    while True:
        operator = input('Please select an operator: ')
        # if valid, break loop and continue main loop
        if operator in operators:
            break
        # if invalid, display valid options and prompt for re-entry
        else:
            print(f'Valid operators are: {", ".join(operators)}')
    # loop to accept and validate digits
    while True:
        x = input('What is the first number? ')
        y = input('What is the second number? ')
        # attempt to convert to int or float
        try:
            x = int_or_flt(x)
            y = int_or_flt(y)
            break
        # prompt for re-entry if either fails
        except:
            print('Enter your responses as a number.')
    # display results
    print(f'{x} {operator} {y} = {maths(x,y,operator)}')
    break
'''


# Version 2
'''
def int_or_flt(input):
    """
    Converts to integer if whole number, otherwise returns float
    Also tries to eliminate floating point errors
    """
    # split input for floating point error detection
    x = str(input).split('.')
    # if whole number, return an int
    if float(input) % 1 == 0:
        return int(input)
    # if floating point error detected, use round to correct
    elif '9999' in x[1]:
        return round(float(input),(x[1].find('9999')))
    # otherwise, return a float
    else:
        return float(input)


def maths(x,y,operator):
    """
    Performs basic arithmatic based on input operator
    """
    # perform and return maths
    if operator == '+':
        return int_or_flt(x + y)
    elif operator == '-':
        return int_or_flt(x - y)
    elif operator == '*':
        return int_or_flt(x * y)
    elif operator == '/':
        return int_or_flt(x / y)

# list of operators for validation
operators = ['+','-','*','/']

while True:
    # variable to escape nested loop
    break_out = False
    # loop to accept and validate operator input
    while True:
        operator = input('Please select an operator or type "done" to quit: ')
        # if valid, break loop and continue main loop
        if operator in operators:
            break
        # if user wants to quit, set variable to True
        elif operator.lower() == 'done':
            break_out = True
            print('Goodbye!')
            break
        # if invalid, display valid options and prompt for re-entry
        else:
            print(f'Valid operators are: {", ".join(operators)}')
    # exit loop if user chose to above
    if break_out == True:
        break
    # loop to accept and validate digits
    while True:
        x = input('What is the first number? ')
        y = input('What is the second number? ')
        # attempt to convert to int or float
        try:
            x = int_or_flt(x)
            y = int_or_flt(y)
            break
        # prompt for re-entry if either fails
        except:
            print('Enter your responses as a number.')
    # display results
    print(f'{x} {operator} {y} = {maths(x,y,operator)}')
'''


# Version 3

def int_or_flt(input):
    """
    Converts to integer if whole number, otherwise returns float
    Also tries to eliminate floating point errors
    """
    # split input for floating point error detection
    x = str(input).split('.')
    # if whole number, return an int
    if float(input) % 1 == 0:
        return int(input)
    # if floating point error detected, use round to correct
    elif '9999' in x[1]:
        return round(float(input),(x[1].find('9999')))
    # otherwise, return a float
    else:
        return float(input)


def maths(x,y,operator):
    """
    Performs basic arithmatic based on input operator
    """
    # perform and return maths
    return int_or_flt(eval(str(x) + operator + str(y)))

# list of operators for validation
operators = ['+','-','*','/']

while True:
    # variable to escape nested loop
    break_out = False
    # loop to accept and validate operator input
    while True:
        operator = input('Please select an operator or type "done" to quit: ')
        # if valid, break loop and continue main loop
        if operator in operators:
            break
        # if user wants to quit, set variable to True
        elif operator.lower() == 'done':
            break_out = True
            print('Goodbye!')
            break
        # if invalid, display valid options and prompt for re-entry
        else:
            print(f'Valid operators are: {", ".join(operators)}')
    # exit loop if user chose to above
    if break_out == True:
        break
    # loop to accept and validate digits
    while True:
        x = input('What is the first number? ')
        y = input('What is the second number? ')
        # attempt to convert to int or float
        try:
            x = int_or_flt(x)
            y = int_or_flt(y)
            break
        # prompt for re-entry if either fails
        except:
            print('Enter your responses as a number.')
    # display results
    print(f'{x} {operator} {y} = {maths(x,y,operator)}')