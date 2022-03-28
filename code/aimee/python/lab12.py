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
for i in (range(1, len(lines))): # starting from list 1 
    values.append(lines[i].split(','))
    
# for loop to reference value in values, then zip those values with the keys list
pets = [{key:value for key, value in zip(keys, value)} for value in values]

# ---------------------------------------------- #
'''VERSION TWO: REPL'''
# ---------------------------------------------- #

# FUNCTIONS -------------------------- #

def new_record():
    '''Create a new record'''
    name = input('\nEnter your pet\'s name: ')
    age = input('\nEnter their age: ')
    breed = input('\nEnter their breed: ')
    color = input('\nEnter their coat color: ')
    coat_length = input('\nEnter their coat length: ')
    activity = input('\nEnter their favorite activity: ')
    
    # add user's input to list of dictionaries 
    new_values = [name, age, breed, color, coat_length, activity]

    new_pet = [{key:value for key, value in zip(keys, values)} for value in values]
    # this assigned each letter to a key instead of by word
    # {'name': 'w', 'age': 'a', 'breed': 'l', 'color': 't', 'coat-length': 'e', 'favorite-activity': 'r'}
   
    return new_pet

print(new_record()) 
























# # Lab 12, Contact List ---- #

# with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pets.csv', 'r') as file:
#     lines = file.read().split('\n') # gives a list without new line characters

# # ---------------------------------------------- #
# '''VERSION ONE: LIST'''
# # ---------------------------------------------- #

# headers = lines[0]
# axel = lines[1]
# juniper = lines[2]
# wesley = lines[3]
# violet = lines[4]

# # for line in lines[1:]:
# #     pet = line.split(',')
# #     print(pet)

# # create lists of each value
# headers = headers.split(',')
# axel = axel.split(',')
# juniper = juniper.split(',')
# wesley = wesley.split(',')
# violet = violet.split(',')

# axel_dict = {}
# axel_dict[headers[0]] = axel[0]
# axel_dict[headers[1]] = axel[1]
# axel_dict[headers[2]] = axel[2]
# axel_dict[headers[3]] = axel[3]
# axel_dict[headers[4]] = axel[4]
# axel_dict[headers[5]] = axel[5]

# juniper_dict = {}
# juniper_dict[headers[0]] = juniper[0]
# juniper_dict[headers[1]] = juniper[1]
# juniper_dict[headers[2]] = juniper[2]
# juniper_dict[headers[3]] = juniper[3]
# juniper_dict[headers[4]] = juniper[4]
# juniper_dict[headers[5]] = juniper[5]

# wesley_dict = {}
# wesley_dict[headers[0]] = wesley[0]
# wesley_dict[headers[1]] = wesley[1]
# wesley_dict[headers[2]] = wesley[2]
# wesley_dict[headers[3]] = wesley[3]
# wesley_dict[headers[4]] = wesley[4]
# wesley_dict[headers[5]] = wesley[5]

# violet_dict = {}
# violet_dict[headers[0]] = violet[0]
# violet_dict[headers[1]] = violet[1]
# violet_dict[headers[2]] = violet[2]
# violet_dict[headers[3]] = violet[3]
# violet_dict[headers[4]] = violet[4]
# violet_dict[headers[5]] = violet[5]


# pets = []
# pets.append(axel_dict)
# pets.append(juniper_dict)
# pets.append(wesley_dict)
# pets.append(violet_dict)
# print(pets)

# # ---------------------------------------------- #
# '''VERSION TWO: REPL'''
# # ---------------------------------------------- #

# # FUNCTIONS -------------------------- #

# def new_record(): # writing
#     '''Create a new record'''
#     k_name = headers[0]
#     v_name = input('Enter your pet\'s name: ')
    
#     k_age = headers[1]
#     v_age = input('Enter their age: ')

#     k_breed = headers[2]
#     v_breed = input('Enter their breed: ')

#     k_color = headers[3]
#     v_color = input('Enter their coat color: ')

#     k_coat = headers[4]
#     v_coat = input('Enter their coat length: ')

#     k_activity = headers[5]
#     v_activity = input('Enter their favorite activity: ')
    
#     new_record = [
#         {k_name:v_name}, 
#         {k_age:v_age}, 
#         {k_breed:v_breed},
#         {k_color:v_color},
#         {k_coat:v_coat},
#         {k_activity:v_activity},
#         ]
#     pets.append(new_record) # add new record to pets list
#     with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/new-pets.csv', 'w') as f:
#         f.write() # TypeError: write() argument must be str, not list
    

    
# def retrieve(): # not writing anything, just reading
#     '''Retrieve an existing record'''
#     user_input = input('Which pet are you looking for? ').lower()
#     for pet in pets:
#         if user_input in pet['name'].lower():
#              return pet['name'].title() + ', age ' + pet['age'] + ', is a ' + pet['color'] + ' ' + \
#              pet['breed'] + ' with a ' + pet['coat length'] + ' haired coat. They love '\
#             + pet['favorite activity'] + '.'

# def update(): # writing
#     '''Update a record''' # works
#     user_input = input('Enter the name of the pet you want to update: ').lower()
#     for pet in pets:
#         if user_input in pet['name'].lower():
#             user_update = input('\nWhat would you like to update? The categories are ' \
#                 'name, age, color, breed, coat length, favorite activity: ')
#             if user_update == 'name':
#                 pet['name'] = input('\nEnter the new name: ') 
#                 return '\nThe record has been updated.\n'               
#             elif user_update == 'age':
#                 pet['age'] = input('\nEnter the new age: ') 
#                 return '\nThe record has been updated.\n'              
#             elif user_update == 'color':
#                 pet['color'] = input('\nEnter the new color: ')
#                 return '\nThe record has been updated.\n'                
#             elif user_update == 'breed':
#                 pet['breed'] = input('\nEnter the new breed: ')  
#                 return '\nThe record has been updated.\n'              
#             elif user_update == 'coat length':
#                 pet['coat length'] = input('\nEnter the new coat length: ')
#                 return '\nThe record has been updated.\n'                
#             elif user_update == 'favorite activity':
#                 pet['favorite activity'] = input('\nEnter the new favorite activity: ')
#                 return '\nThe record has been updated.\n'                
#             else: 
#                 if user_input not in pet['name'].lower():
#                     return '\nThat name is not currently in the database. Please add a new record.'
#                 break
#     with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/new-pets.csv', 'w') as f:
#         f.write()      
#     # return 'Taking you back to the main menu.'

# def delete(): 
#     user_input = input('Enter the name of the pet record you would like to delete: ').lower()
#     for i in range(len(pets)):
#         if pets[i]['name'] == user_input:
#             del pets[i]        
#         else:
#             break
#     deleted = pets
#     # having issues getting "name not found" to work
#     # if pets[i]['name'] != user_input:
#             # print('That name is not currently in the database. Please try again.')
#         # break
#     with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/new-pets.csv', 'w') as f:
#         f.write(deleted)
#     # return 'The record called ' + user_input.title() + ' has been deleted.' + '\n' + '*'*78

    

# REPL ----------- #

# for x in pets:
#     print('Welcome to the pet information database! Please select from the following options: ')
#     print('\n' + '*'*78)
#     print('(c)reate new record | (r)etrieve record | (u)pdate a record | (d)elete record | (e)xit')
#     print('\n' + '*'*78)
#     command = input('Enter the letter corresponding to your selected option: ').lower()
#     print('\n')

#     if command == 'c':
#         print(new_record())
#     elif command == 'r':
#         print(retrieve())
#     elif command == 'u':
#         print(update())
#     elif command == 'd':
#         print(delete())        
#     elif command == 'e':
#         print('Exiting the database.')
#         break
#     else:
#         print('\nPlease select a valid option\n')

