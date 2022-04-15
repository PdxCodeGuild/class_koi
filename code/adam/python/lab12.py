# Lab 12 - Contact List
# Version 1

import csv

with open('data/contacts.csv','r') as csv_contacts:
    lines = csv_contacts.read().split('\n')
    # print(lines)

headers = lines[0]
headers = headers.split(',')
# print(headers)

contacts_list = []
character_dict = {}
character_list = []
for line in lines[1:]:
    character_dict = {}
    character_list = line.split(',')
    for i, key in enumerate(headers):
        character_dict[key] = character_list[i]
    contacts_list.append(character_dict)
# print(contacts_list)

#---------------------------------------------------------------------
# Version 2

# function to Create a new contact: ask the user for each attribute, 
# add a new contact to your contact list with the attributes that the user entered 
contact_list = []
character_dict = {}
def create():
    print('\nCreating a new contact.\n')
    name = input('Enter the NAME of the contact: ').title()
    contact_list.append(name)
    city = input('Enter the CITY of the contact: ').title()
    contact_list.append(city)
    state = input('Enter the STATE of the contact: ').title()
    contact_list.append(state)
    age = input('Enter the AGE of the contact: ')
    contact_list.append(age)
    favorite_food = input('Enter the FAVORITE FOOD of the contact: ')
    contact_list.append(favorite_food)
    favorite_beverage = input('Enter the FAVORITE BEVERAGE of the contact: ')
    contact_list.append(favorite_beverage)
    # print(contact_list)
    for i, key in enumerate(headers):
        character_dict[key] = contact_list[i]
    contacts_list.append(character_dict)
    print(character_dict)
    return

# function to Retrieve a contact: ask the user for the contact's name, 
# find the user with the given name, and display their information
def retrieve():
    search_name = input('Enter the name of the contact to retrieve: ').lower()
    for contact in contacts_list:
        if search_name in contact['name'].lower():
            print(contact)
            return
    print('\nContact not found\n')

# fucntion to Update a contact: ask the user for the contact's name, 
# then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update():
    update_name = input('Enter the name of the contact to update: ').lower()
    for contact in contacts_list:
        if update_name in contact['name'].lower():
            update_choice = input(f"What would you like to update for '{contact['name']}' [c]ity, [s]tate, [a]ge, [f]ood, or [b]everage? ").lower()
            if update_choice == 'c':
                update_var = input('Enter the new city: ').lower()
                contact['city'] = update_var.title()
                print(contact)
            elif update_choice == 's':
                update_var = input('Enter the new state: ').lower()
                contact['state'] = update_var.title()
                print(contact)
            elif update_choice == 'a':
                update_var = input('Enter the new age: ')
                contact['age'] = update_var
                print(contact)
            elif update_choice == 'f':
                update_var = input('Enter the new favorite food: ')
                contact['favorite food'] = update_var
                print(contact)
            elif update_choice == 'b':
                update_var = input('Enter the new favorite beverage: ')
                contact['favorite beverage'] = update_var
                print(contact)
                return

# function to Delete a contact: ask the user for the contact's name, 
# remove the contact with the given name from the contact list.
def remove():
    remove_name = input('Enter the name to remove from contacts: ').lower()
    for contact in contacts_list:
        if remove_name in contact['name'].lower():
            valid_remove = input(f"Are you sure you want to delete the contact '{contact['name']}', [y]es or [n]o : ").lower()
            if valid_remove == 'y':
                contacts_list.remove(contact)
                print(contacts_list)
            else:
                print(contacts_list)
                return

# Version 3
# When REPL loop finishes, write the updated contact info to the CSV file to be saved.
# function to write updated contact info to contacts.csv file
def write_to_file():
    headers_sentence = ','.join(headers) # name,city,state,age,favorite food,favorite beverage
    contacts_list_sentences= []
    contacts_list_sentences.append(headers_sentence)

    for contact in contacts_list:
        contact_values = contact.values()
        contact_sentence = ','.join(contact_values)
        contacts_list_sentences.append(contact_sentence)
    updated_contacts_csv = '\n'.join(contacts_list_sentences)

    with open('data/contacts.csv', 'w') as f:
        f.write(updated_contacts_csv)

while True:
    choice = input('Would you like to [c]reate, [r]etrieve, [u]pdate, or [d]elete a contact or [q]uit? ').lower()
    if choice not in ['c' ,'r', 'u', 'd', 'q']:
        print('Please enter [c] for create, [r] for remove, [u] for update, [d] for delete or [q] to quit: ')
    if choice == 'q':
        print('\nContacts list .csv file will be updated with any changes.')
        break
    if choice == 'c':
        create()
    if choice == 'r':
        retrieve()
    if choice == 'u':
        update()
    if choice == 'd':
        remove()
# call and run function to write updated contacts list of dictionaries as csv file
write_to_file()
