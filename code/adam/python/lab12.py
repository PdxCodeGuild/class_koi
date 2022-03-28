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

# Create a record: ask the user for each attribute, 
# -add a new contact to your contact list with the attributes that the user entered 
contact_list = []
character_dict = {}
def create():
    name = input('Enter the NAME of the contact: ')
    contact_list.append(name)
    city = input('Enter the CITY of the contact: ')
    contact_list.append(city)
    state = input('Enter the STATE of the contact: ')
    contact_list.append(state)
    age = input('Enter the AGE of the contact: ')
    contact_list.append(age)
    favorite_food = input('Enter the FAVORITE FOOD of the contact: ')
    contact_list.append(favorite_food)
    favorite_beverage = input('Enter the FAVORITE BEVERAGE of the contact: ')
    contact_list.append(favorite_beverage)
    for i, key in enumerate(headers):
        character_dict[key] = contact_list[i]
    contacts_list.append(character_dict)
    return

# Retrieve a record: ask the user for the contact's name, 
# find the user with the given name, and display their information
def retrieve():
    search_name = input('Enter the name of the contact: ').lower()
    for contact in contacts_list:
        # print(contact['name'].title())
        if search_name in contact['name'].lower():
            # contacts_list.index(search_name)
            print(contact)
            return
    print('Contact not found')

retrieve() 
# print(contacts_list)



# while True:
#     choice = input('[C]reate, 

