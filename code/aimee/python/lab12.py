# Lab 12, Contact List ---- #

with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pets.csv', 'r') as file:
    lines = file.read().split('\n') # gives a list without new line characters

# ---------------------------------------------- #
'''VERSION ONE: LIST'''
# ---------------------------------------------- #

headers = lines[0]
axel = lines[1]
juniper = lines[2]
wesley = lines[3]
violet = lines[4]

# create lists of each value
headers = headers.split(',')
axel = axel.split(',')
juniper = juniper.split(',')
wesley = wesley.split(',')
violet = violet.split(',')

axel_dict = {}
axel_dict[headers[0]] = axel[0]
axel_dict[headers[1]] = axel[1]
axel_dict[headers[2]] = axel[2]
axel_dict[headers[3]] = axel[3]
axel_dict[headers[4]] = axel[4]
axel_dict[headers[5]] = axel[5]

juniper_dict = {}
juniper_dict[headers[0]] = juniper[0]
juniper_dict[headers[1]] = juniper[1]
juniper_dict[headers[2]] = juniper[2]
juniper_dict[headers[3]] = juniper[3]
juniper_dict[headers[4]] = juniper[4]
juniper_dict[headers[5]] = juniper[5]

wesley_dict = {}
wesley_dict[headers[0]] = wesley[0]
wesley_dict[headers[1]] = wesley[1]
wesley_dict[headers[2]] = wesley[2]
wesley_dict[headers[3]] = wesley[3]
wesley_dict[headers[4]] = wesley[4]
wesley_dict[headers[5]] = wesley[5]

violet_dict = {}
violet_dict[headers[0]] = violet[0]
violet_dict[headers[1]] = violet[1]
violet_dict[headers[2]] = violet[2]
violet_dict[headers[3]] = violet[3]
violet_dict[headers[4]] = violet[4]
violet_dict[headers[5]] = violet[5]


pets = []
pets.append(axel_dict)
pets.append(juniper_dict)
pets.append(wesley_dict)
pets.append(violet_dict)
#print(pets)

# ---------------------------------------------- #
'''VERSION TWO: REPL'''
# ---------------------------------------------- #

# FUNCTIONS -------------------------- #
def new_record():
    '''Create a new record'''
    k_name = headers[0]
    v_name = input('Enter your pet\'s name: ')
    
    k_age = headers[1]
    v_age = input('Enter their age: ')

    k_breed = headers[2]
    v_breed = input('Enter their breed: ')

    k_color = headers[3]
    v_color = input('Enter their coat color: ')

    k_coat = headers[4]
    v_coat = input('Enter their coat length: ')

    k_activity = headers[5]
    v_activity = input('Enter their favorite activity: ')
    
    new_record = [
        {k_name:v_name}, 
        {k_age:v_age}, 
        {k_breed:v_breed},
        {k_color:v_color},
        {k_coat:v_coat},
        {k_activity:v_activity},
        ]
    return new_record

def retrieve():
    '''Retrieve an existing record'''
    user_input = input('Which pet are you looking for? ').lower()
    for pet in pets:
        if user_input in pet['name'].lower():
             return pet['name'].title() + ', age ' + pet['age'] + ', is a ' + pet['color'] + ' ' + \
             pet['breed'] + ' with a ' + pet['coat length'] + ' haired coat. They love '\
            + pet['favorite activity'] + '.'

def update():
    '''Update part of a record'''
    user_input = input('Enter the name of the pet you want to update: ').lower()
    for pet in pets:
        if user_input in pet['name'].lower():
            user_update = input('')


# to print for REPL: print('\n' + '*'*80)


# Update a record

# Delete a record


# REPL ----------- #
