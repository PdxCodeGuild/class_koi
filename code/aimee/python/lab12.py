# Lab 12 attempt 2, Contact List ---- #

with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pets.csv', 'r') as file:
    lines = file.read().split('\n') # gives a list without new line characters

# ---------------------------------------------- #
'''VERSION ONE: CONVERT TO DICTIONARY'''
# ---------------------------------------------- #

# get keys for dictionary (the headers)
keys = lines[0].split(',')

# get values by iterating through each list/line
values = []
for i in (range(1, len(lines))): # starting from list 1, 0 being the keys (headers)
    values.append(lines[i].split(','))
    
# for loop to reference value in values, then zip those values with the keys list
pets = [{key:value for key, value in zip(keys, value)} for value in values]


# ---------------------------------------------- #
'''VERSION TWO: REPL'''
# ---------------------------------------------- #

# FUNCTIONS -------------------------- #

def write():
    '''writes to csv file'''
    dictionary = ','.join(keys) + '\n'
    for pet in pets:        
        dictionary += ','.join(list(pet.values())) + '\n'
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pets.csv', 'w') as f:
        f.write(dictionary)

def create(): # WORKS!
    '''Create a new record'''
    name = input('\nEnter your pet\'s name: ')
    age = input('\nEnter their age: ')
    breed = input('\nEnter their breed: ')
    color = input('\nEnter their coat color: ')
    coat_length = input('\nEnter their coat length: ')
    activity = input('\nEnter their favorite activity: ')
    
    # add user's input to list of dictionaries 
    new_values = [name, age, breed, color, coat_length, activity] # create list of new values

    # combine keys list with new_values list, then append to pets (list of dicts)
    result = {}
    for key in keys:
        for value in new_values:
            result[key] = value
            new_values.remove(value)
            break
    
    # add new dictionary to pets, convert to string in order to write file
    pets.append(result)
    new_pets = '\n'.join([str(x) for x in pets])
    
    return '\n' + name.upper() + ' has been added. Returning to the main menu...\n' + '-'*78

def retrieve():
    '''Retrieve an existing record'''
    pet_to_find = input('Which pet are you looking for? ').lower()
    for pet in pets:
        if pet_to_find in pet['name'].lower():
            return '\n' + pet['name'].title() + ', age ' + pet['age'] + ', is a ' + pet['color'] + ' ' + \
              pet['breed'] + ' with a ' + pet['coat-length'] + ' haired coat. They love '\
             + pet['favorite-activity'] + '.' + '\n\nReturning to the main menu...\n' + '-'*78
        
    return '\n***ERROR: That pet isn\'t in this database. Please create a new record.***'
        

def update(): 
    '''Update a record''' 
    user_input = input('Enter the name of the pet you want to update: ').lower()
    for pet in pets:
        if user_input in pet['name'].lower():
            user_update = input('\nWhat would you like to update? The categories are: ' \
                '\n* name, \n* age, \n* color, \n* breed, \n* coat length, '\
                    '\n* favorite activity \nYour selection: ')            
            if user_update == 'name':
                pet['name'] = input('\nEnter the new name: ').lower() 
                return '\nThe record has been updated.\n' + '-'*78                
            elif user_update == 'age':
                pet['age'] = input('\nEnter the new age: ').lower() 
                return '\nThe record has been updated.\n' + '-'*78               
            elif user_update == 'color':
                pet['color'] = input('\nEnter the new color: ').lower()
                return '\nThe record has been updated.\n' + '-'*78                 
            elif user_update == 'breed':
                pet['breed'] = input('\nEnter the new breed: ').lower()  
                return '\nThe record has been updated.\n' + '-'*78             
            elif user_update == 'coat-length':
                pet['coat-length'] = input('\nEnter the new coat length: ').lower()
                return '\nThe record has been updated.\n' + '-'*78                 
            elif user_update == 'favorite-activity':
                pet['favorite-activity'] = input('\nEnter the new favorite activity: ').lower()
                return '\nThe record has been updated.\n' + '-'*78

    new_pets = '\n'.join([str(x) for x in pets])
    
    return '\n***ERROR: That name is not in the database. Returning to the main menu...***'

def delete(): 
    '''Deletes a record'''
    pet_to_delete = input('Enter the name of the pet record you would like to delete: ').lower()
    for x in range(len(pets)):
        if pets[x]['name'] == pet_to_delete:
            del pets[x]
            return '\nThe record called ' + pet_to_delete.title() + ' has been deleted.' + '\n\n' + \
                'Returning to the main menu...\n' + '-'*78

    return '\n***ERROR: That name is not currently in the database. Returning to the main menu...***\n' \
                + '-'*78


# REPL ------------------------------- #

while True:
    print('\nWelcome to the pet information database! Please select from the following options: ')
    print('\n' + '*'*78)
    print('(c)reate new record | (r)etrieve record | (u)pdate a record | (d)elete record | (e)xit')
    print('\n' + '*'*78)
    command = input('Enter the letter corresponding to your selected option: ').lower()
    print('\n')

    if command == 'c':
        print(create())
    elif command == 'r':
        print(retrieve())
    elif command == 'u':
        print(update())
    elif command == 'd':
        print(delete())            
    elif command == 'e':
        print('Saving your changes and exiting the database.')
        break
    else:
        print('\nPlease select a valid option\n')
    
write()
