'''
PDX Code Guild - Class Koi
Input Validation Module
Matt Walsh
'''

def valid_str(prompt,choices,error=None,case_sensitive=True,return_case=None):
    """
    Prompt for and validate string input against a list of choices:
    -   (required) prompt is the string that will prompt the user for input
    -   (required) choices is a list of valid choices
    -   (optional) error is the error message displayed if invalid
    -   (optional) case_sensitive uses bool to validate with/without case-sensitivity (default is case-sensitive)
    -   (optional) return_case allows the string to be returned with built-in string case methods
    -   Use None as needed for default functionality of optional arguments
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
            for i in range(len(choices)):
                choices[i] = choices[i].lower()
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

def valid_int(prompt=None,error=None,min=None,max=None):
    """
    Prompt for and validate integer input by attempting to convert string to integer
    -   (optional) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) min is the smallest integer accepted (inclusive)
    -   (optional) max is the largest integer accepted (inclusive)
    -   Use None as needed for default functionality of optional arguments
    """
    # set input prompt if blank
    if prompt is None:
        prompt = 'Please enter a number: '
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

def valid_flt(prompt=None,error=None,min=None,max=None,rounded=None):
    """
    Prompt for and validate float input by attempting to convert string to float
    -   (optional) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) min is the smallest float accepted (inclusive)
    -   (optional) max is the largest float accepted (inclusive)
    -   (optional) rounded is the number of decimal points to round the result to
    -   Use None as needed for default functionality of optional arguments
    """
    # set input prompt if blank
    if prompt is None:
        prompt = 'Please enter a number: '
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
            elif user_input >= min and user_input <= max:
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

def valid_int_flt_lite(num,valid_type=None):
    """
    Basic integer or float validation
    -   (required) num is the input number to validate
    -   (optional) valid_type is int or float (will choose if unspecified)
    -   Use None as needed for default functionality of optional arguments
    -   Returns False if invalid
    """
    try:
        if valid_type is int:
            return int(num)
        elif valid_type is float:
            return float(num)
        else:
            return int(num) if num % 1 == 0 else float(num)
    except:
        return False

def valid_list(prompt=None,error=None,item_type=None,min_length=None,max_length=None,delimiter=','):
    """
    Validate and convert list input by attempting to convert string to list
    -   (optional) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) item_type is the type to convert list items to (default will return list of strings)
    -   (optional) min_length is the minimum number of items in the list
    -   (optional) max_length is the maximum number of items in the list
    -   (optional) delimiter is the seperator to look for
    -   Use None as needed for default functionality of optional arguments
    """
    # set input prompt if blank
    if prompt is None:
        prompt = f'Please enter a list separated by "{delimiter}": '
    # continue looping until valid input is given
    while True:
        # set/reset int/flt validation error flag
        int_flt_error = False
        # prompt for input
        user_input = input(prompt)
        # strip brackets if they exist and split at delimiter
        user_input = user_input.strip('][}{)(').split(delimiter)
        # iterate through items on list and strip leading/trailing whitespace
        for i in range(len(user_input)):
            user_input[i] = user_input[i].strip()
            # convert to int or float if chosen and valid
            if item_type is int or item_type is float:
                # # set error flag and break if validation fails
                if valid_int_flt_lite(user_input[i],item_type) is False:
                    int_flt_error = True
                    break
                else:
                    user_input[i] = valid_int_flt_lite(user_input[i],item_type)
        # reset if error triggered above
        if int_flt_error:
            if error is None:
                print('An error has occurred.')
            else:
                print(error)
            continue
        # return list if min/max length not specified
        if min_length is None and max_length is None:
            return user_input
        # setup variables for min/max check
        item_items = 'item' if len(user_input) == 1 else 'items'
        too_short = f'You entered {len(user_input)} {item_items}, but the minimum is {min_length}.'
        too_long = f'You entered {len(user_input)} {item_items}, but the maximum is {max_length}.'
        if min_length is None:
            min_length = len(user_input)
        if max_length is None:
            max_length = len(user_input)
        # check against min/max length
        if len(user_input) < min_length or len(user_input) > max_length:
            if len(user_input) < min_length:
                print(too_short)
            if len(user_input) > max_length:
                print(too_long)
        else:
            return user_input

def valid_dict(prompt=None,error=None,num_dicts=1,key_type=None,value_type=None,key_value_delimiter=':',pair_delimiter=','):
    """
    Validate and convert dictionary input by attempting to convert string to dictionary
    Supports construction of list of dictionaries
    -   (optional) prompt is the string that will prompt the user for input
    -   (optional) error is the error message displayed if invalid
    -   (optional) num_dicts is the number of dictionaries you would like to create within a list (default: 1, not in a list)
    -   (optional) key_type is the type to convert keys to (default: string)
    -   (optional) value_type is the type to convert values to (default: string)
    -   (optional) key_value_split is the delimiter between keys and values (default: ':')
    -   (optional) pair_split is the delimiter between pairs (default: ',')
    """
    # check to make sure key/value and pair delimiters don't match
    if key_value_delimiter == pair_delimiter:
        print(f'Error: both delimiters are set to "{pair_delimiter}".')
        pass
    else:
        print(f'Enter dictionaries with keys/values separated by "{key_value_delimiter}" and pairs separated by "{pair_delimiter}".')
    # create empty list if necessary
    if num_dicts > 1:
        new_list = []
    # variables to modify dictionary prompts and loop specified number of times
    first_loop = True
    num_loops = num_dicts
    # loop number of times specified in num_dicts
    while num_loops > 0:
        num_loops -= 1
        # create/reset dictionary
        new_dict = {}
        # set/reset error flag variables
        pair_error = False
        int_flt_error = False
        # display default or specified prompt
        if prompt is None:
            # setup variable to improve prompt then display
            if num_dicts == 1:
                first_last_next = 'a'
            elif first_loop:
                first_last_next = 'the first'
            elif num_loops == 0:
                first_last_next = 'the last'
            else:
                first_last_next = 'the next'
            user_input = input(f'Please enter {first_last_next} dictionary: ')
        else:
            # display specified prompt
            user_input = input(prompt)
        # strip brackets if they exist and split at delimiter
        user_input = user_input.strip('][}{)(').split(pair_delimiter)
        # iterate through items on list and strip leading/trailing whitespace
        for i in range(len(user_input)):
            user_input[i] = user_input[i].strip()
            # split resulting pairs
            user_input[i] = user_input[i].strip('][}{)(').split(key_value_delimiter)
            # check to make sure a pair exists
            if len(user_input[i]) != 2:
                pair_error = True
                break
            # check to make sure a pair exists
            if len(user_input[i]) != 2 and error is None:
                print(f'"{user_input[i]}" is not a valid pair.')
                break
            elif len(user_input[i]) != 2:
                print(error)
                break
            # convert key to int or float if chosen an valid
            if key_type is int or key_type is float:
                # display error if validation fails
                if valid_int_flt_lite(user_input[i][0],key_type) is False:
                    # set variable to trigger reset
                    int_flt_error = True
                    break
                else:
                    user_input[i][0] = valid_int_flt_lite(user_input[i][0],key_type)
            # convert value to int or float if chosen and valid
            if value_type is int or value_type is float:
                # display error if validation fails
                if valid_int_flt_lite(user_input[i][1],value_type) is False:
                    # set variable to trigger reset
                    int_flt_error = True
                    break
                else:
                    user_input[i][1] = valid_int_flt_lite(user_input[i][1],value_type)
            # add to dictionary
            new_dict[user_input[i][0]] = user_input[i][1]
        # catch errors and reset
        if pair_error:
            if error is None:
                print(f'"{user_input[i]}" is not a valid pair.')
            else:
                print(error)
            num_loops += 1
            continue
        if int_flt_error:
            if error is None:
                print('An error has occurred.')
            else:
                print(error)
            num_loops += 1
            continue
        # add to list if more than one dictionary
        if num_dicts > 1:
            new_list.append(new_dict)
        first_loop = False
    # return list of dictionaries if multiple
    if num_dicts > 1:
        return new_list
    # otherwise return single dictionary
    else:
        return new_dict