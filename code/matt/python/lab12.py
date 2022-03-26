'''
PDX Code Guild - Class Koi
Lab 12 - Contact List
Matt Walsh
'''


# Version 1
'''
# open csv and generate list of each row
with open('code/matt/python/lab12.csv') as csv_states:
    rows = csv_states.read().split('\n')

# grab column names from list
columns = rows[0].split(',')
# empty list to hold states
states = []
# iterate through each row except the first
for row in rows[1:]:
    # split row string into list
    row = row.split(',')
    # empty dictionary to construct each state
    state_dict = {}
    # iterate through each item
    for i in range(len(row)):
        state_dict[columns[i]] = row[i]
    # add state to list as dictionary
    states.append(state_dict)

print(states)
'''


# Version 2
'''
# import custom module - run from class_koi
import sys
sys.path.append('./code/matt/python/modules')
from input_validation import valid_str

def csv_to_dict():
    """
    Converts csv to list of dictionaries
    """
    # open csv and generate list of each row
    with open('code/matt/python/lab12.csv') as csv_states:
        rows = csv_states.read().split('\n')

    # grab column names from list
    columns = rows[0].split(',')
    # empty list to hold states
    states = []
    # iterate through each row except the first
    for row in rows[1:]:
        # split row string into list
        row = row.split(',')
        # empty dictionary to construct each state
        state_dict = {}
        # iterate through each item
        for i in range(len(row)):
            state_dict[columns[i]] = row[i]
        # add state to list as dictionary
        states.append(state_dict)
    return states, columns

def gen_state_list():
    """
    Generates list of states for use in REPL
    """
    state_list = []
    for state in states:
        state_list.append(state['state'])
    return state_list

def create(name):
    """
    Creates new dictionary entries
    """
    # dictionary to hold new state
    new_state = {'state':name.title()}
    # iterate through columns
    for column in columns[1:]:
        # Prompt for entry per column
        new_state[column] = input(f'What is the {column} for {name.title()}? ')
    # add to list of dictionaries
    states.append(new_state)
    pass

def retrieve(name):
    """
    Looks up and displays dictionary entries
    """
    # iterate through list of states and check for name match
    for state in states:
        if state['state'].lower() == name.lower():
            # display results
            print(f'\nHere is the information I could find about {name.title()}:\n{state}\n')
    pass

def update(name):
    """
    Modifies existing dictionary entries
    """
    # iterate through list of states and check for name match
    for i in range(len(states)):
        if states[i]['state'].lower() == name.lower():
            # update parameters for loop
            prompt = 'What would you like to update? '
            error = 'That is not a valid option. Enter L to view options, and D when done.'
            choices = columns
            choices.extend(['l','d'])
            # ask which item(s) to update and keep looping until done
            while True:
                action = valid_str(prompt,choices,error,False,'lower')
                # list columns
                if action == 'l':
                    print(', '.join(columns[:-2]))
                # exit loop
                elif action == 'd':
                    break
                # display current data and prompt for modification
                elif action in columns:
                    print(f'Current {action} is {states[i][action.lower()]}')
                    states[i][action.lower()] = input(f'Please enter the new {action} for {name}: ')
    pass

def delete(name):
    """
    Deletes dictionary entries
    """
    # iterate through list of states and check for name match
    for i in range(len(states)):
        if states[i]['state'].lower() == name.lower():
            # update parameters for valid_str
            prompt = f'{name.title()} is about to be deleted. Are you sure you want to do this? Y/N: '
            choices = ['y','n']
            # ask for confirmation before deleting
            confirm = valid_str(prompt,choices,None,False,'lower')
            if confirm == 'y':
                states.pop(i)
    pass

# generate lists of states and columns from csv
states = csv_to_dict()[0]
columns = csv_to_dict()[1]

# CRUD REPL
while True:
    # generate and store list of states
    state_names = gen_state_list()
    # store parameters for valid_str
    prompt = 'Would you like to [C]reate, [R]etrieve, [U]pdate, or [D]elete a state? '
    choices = ['c','r','u','d','l','q']
    error = """"""
To modify a state enter one of the following:
- C to create
- R to retrieve
- U to update
- D to delete

You may also enter L to list current states or Q to quit.
"""
    action = valid_str(prompt,choices,error,False,'lower')
    # update error message for valid_str
    display_states = '\n'.join(state_names)
    error = f'{display_states}\n\nThat state isn\'t on the list. Please choose from a state above.'
    # Create
    if action == 'c':
        create(input('What is the name of the new state? ').lower())
    # Retrieve
    elif action == 'r':
        prompt = 'What is the name of the state you want to look up? '
        retrieve(valid_str(prompt,state_names,error,False,'lower'))
    # Update
    elif action == 'u':
        prompt = 'What is the name of the state you want to update? '
        update(valid_str(prompt,state_names,error,False,'lower'))
    # Delete
    elif action == 'd':
        prompt = 'What is the name of the state you want to delete? '
        delete(valid_str(prompt,state_names,error,False,'lower'))
    # List
    elif action == 'l':
        print('\nCurrent states are:')
        print('\n'.join(state_names),end='\n\n')
    # Quit
    elif action == 'q':
        break
'''


# Version 3

# import custom module - run from class_koi - if issues, uncomment lines 41-77 ########################################################################################################
import sys
sys.path.append('./code/matt/python/modules')
from input_validation import valid_str

def csv_to_dict():
    """
    Converts csv to list of dictionaries
    """
    # open csv and generate list of each row
    with open('code/matt/python/lab12.csv') as csv_states:
        rows = csv_states.read().split('\n')

    # grab column names from list
    columns = rows[0].split(',')
    # empty list to hold states
    states = []
    # iterate through each row except the first
    for row in rows[1:]:
        # split row string into list
        row = row.split(',')
        # empty dictionary to construct each state
        state_dict = {}
        # iterate through each item
        for i in range(len(row)):
            state_dict[columns[i]] = row[i]
        # add state to list as dictionary
        states.append(state_dict)
    return states, columns

def dict_to_csv():
    """
    Converts list of dictionaries back to csv
    """
    # create variable and add columns
    dict_string = ','.join(columns) + '\n'
    # iterate through each state
    for state in states:
        # add each state to string
        dict_string += ','.join(list(state.values())) + '\n'
    # write back to csv
    with open('code/matt/python/lab12.csv','w') as csv_states:
        csv_states.write(dict_string)
    pass

def gen_state_list():
    """
    Generates list of states for use in REPL
    """
    state_list = []
    for state in states:
        state_list.append(state['state'])
    return state_list

def create(name):
    """
    Creates new dictionary entries
    """
    # dictionary to hold new state
    new_state = {'state':name.title()}
    # iterate through columns
    for column in columns[1:]:
        # Prompt for entry per column
        new_state[column] = input(f'What is the {column} for {name.title()}? ')
    # add to list of dictionaries
    states.append(new_state)
    pass

def retrieve(name):
    """
    Looks up and displays dictionary entries
    """
    # iterate through list of states and check for name match
    for state in states:
        if state['state'].lower() == name.lower():
            # display results
            print(f'\nHere is the information I could find about {name.title()}:\n{state}\n')
    pass

def update(name):
    """
    Modifies existing dictionary entries
    """
    # iterate through list of states and check for name match
    for i in range(len(states)):
        if states[i]['state'].lower() == name.lower():
            # update parameters for loop
            prompt = 'What would you like to update? '
            error = 'That is not a valid option. Enter L to view options, and D when done.'
            choices = columns
            choices.extend(['l','d'])
            # ask which item(s) to update and keep looping until done
            while True:
                action = valid_str(prompt,choices,error,False,'lower')
                # list columns
                if action == 'l':
                    print(', '.join(columns[:-2]))
                # exit loop
                elif action == 'd':
                    break
                # display current data and prompt for modification
                elif action in columns:
                    print(f'Current {action} is {states[i][action.lower()]}')
                    states[i][action.lower()] = input(f'Please enter the new {action} for {name}: ')
    pass

def delete(name):
    """
    Deletes dictionary entries
    """
    # iterate through list of states and check for name match
    for i in range(len(states)):
        if states[i]['state'].lower() == name.lower():
            # update parameters for valid_str
            prompt = f'{name.title()} is about to be deleted. Are you sure you want to do this? Y/N: '
            choices = ['y','n']
            # ask for confirmation before deleting
            confirm = valid_str(prompt,choices,None,False,'lower')
            if confirm == 'y':
                states.pop(i)
    pass

# generate lists of states and columns from csv
states = csv_to_dict()[0]
columns = csv_to_dict()[1]

# CRUD REPL
while True:
    # generate and store list of states
    state_names = gen_state_list()
    # store parameters for valid_str
    prompt = 'Would you like to [C]reate, [R]etrieve, [U]pdate, or [D]elete a state? '
    choices = ['c','r','u','d','l','q']
    error = """
To modify a state enter one of the following:
- C to create
- R to retrieve
- U to update
- D to delete

You may also enter L to list current states or Q to quit.
"""
    action = valid_str(prompt,choices,error,False,'lower')
    # update error message for valid_str
    display_states = '\n'.join(state_names)
    error = f'{display_states}\n\nThat state isn\'t on the list. Please choose from a state above.'
    # Create
    if action == 'c':
        create(input('What is the name of the new state? ').lower())
    # Retrieve
    elif action == 'r':
        prompt = 'What is the name of the state you want to look up? '
        retrieve(valid_str(prompt,state_names,error,False,'lower'))
    # Update
    elif action == 'u':
        prompt = 'What is the name of the state you want to update? '
        update(valid_str(prompt,state_names,error,False,'lower'))
    # Delete
    elif action == 'd':
        prompt = 'What is the name of the state you want to delete? '
        delete(valid_str(prompt,state_names,error,False,'lower'))
    # List
    elif action == 'l':
        print('\nCurrent states are:')
        print('\n'.join(state_names),end='\n\n')
    # Quit
    elif action == 'q':
        break

dict_to_csv()