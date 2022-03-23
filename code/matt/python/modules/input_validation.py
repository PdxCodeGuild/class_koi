'''
PDX Code Guild - Class Koi
Input Validation Module
Matt Walsh
'''

def valid_str(prompt,choices,error=None,case_sensitive=True,return_case=None):
    """
    Validate string input against a list of choices:
    -   (required) prompt is the string that will prompt the user for input
    -   (required) choices is a list of valid choices
    -   (optional) error is the error message displayed if invalid
    -   (optional) case_sensitive uses bool to validate with/without case-sensitivity (default is case-sensitive)
    -   (optional) return_case allows the string to be returned with built-in string case methods
    Use None as needed for default functionality of optional arguments
    """
    # list of built-in string case methods
    cases = ['upper','lower','title','capitalize']
    # continue looping until valid input is given
    while True:
        # prompt for input
        user_input = input(prompt)
        # normalizes cases if case-sensitivity has been toggled off
        if not case_sensitive:
            original_input = user_input
            user_input = user_input.lower()
            for choice in choices:
                choice = choice.lower()
        # return input if valid and no return case selected
        if user_input in choices and return_case is None:
            return original_input
        # return input with adjusted case if entered
        elif user_input in choices and return_case in cases:
            return eval("user_input."+return_case+"()")
        # display an error and valid cases if return case entered is invalid
        elif user_input in choices:
            print(f'{return_case} is not a valid method.')
        # display default error message if not specified and input is invalid
        elif error is None:
            print(f'Valid options are: {", ".join(choices)}')
        # display error message if specified and input is invalid
        else:
            print(error)

def valid_int(prompt,error=None,min=None,max=None):
    """
    Validate integer input by attempting to convert string to integer
    -   (required) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) min is the smallest integer accepted (inclusive)
    -   (optional) max is the largest integer accepted (inclusive)
    Use None as needed for default functionality of optional arguments
    """
    # continue looping until valid input is given
    while True:
        # prompt for input
        user_input = input(prompt)
        # attempt to convert to integer
        try:
            user_input = int(user_input)
            # set min and/or max to match user_input if unspecified
            if min is None:
                min = user_input
            if max is None:
                max = user_input
            # return input as integer if within range
            if user_input >= min and user_input <= max:
                return user_input
            # display min/max error message if outside range
            elif user_input > max:
                print(f'{max} is the highest accepted value.')
            elif user_input < min:
                print(f'{min} is the lowest accepted value.')
        # display error if conversion fails
        except:
            # display default error message if not specified
            if error is None:
                print(f'{user_input} is not an integer.')
            # display error message if specified
            else:
                print(error)

def valid_flt(prompt,error=None,min=None,max=None,rounded=None):
    """
    Validate float input by attempting to convert string to float
    -   (required) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) min is the smallest float accepted (inclusive)
    -   (optional) max is the largest float accepted (inclusive)
    -   (optional) rounded is the number of decimal points to round the result to
    Use None as needed for default functionality of optional arguments
    """
    # continue looping until valid input is given
    while True:
        # prompt for input
        user_input = input(prompt)
        # attempt to convert to integer
        try:
            user_input = float(user_input)
            # set min and/or max to match user_input if unspecified
            if min is None:
                min = user_input
            if max is None:
                max = user_input
            # return input as rounded float if within range and round specified
            if user_input >= min and user_input <= max and rounded is not None:
                return round(user_input,rounded)
            # return input as rounded float if within range
            if user_input >= min and user_input <= max:
                return user_input
            # display min/max error message if outside range
            elif user_input > max:
                print(f'{max} is the highest accepted value.')
            elif user_input < min:
                print(f'{min} is the lowest accepted value.')
        # display error if conversion fails
        except:
            # display default error message if not specified
            if error is None:
                print(f'{user_input} is not a number.')
            # display error message if specified
            else:
                print(error)

def valid_lst(prompt,error=None,min_lenth=None,max_length=None,delineator=','):
    """
    Validate list input by attempting to convert string to list
    -   (required) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) min_length is the minimum number of items in the list
    -   (optional) max_length is the maximum number of items in the list
    -   (optional) delineator is the seperator to look for
    Use None as needed for default functionality of optional arguments
    """
    print('not implemented')
    pass

