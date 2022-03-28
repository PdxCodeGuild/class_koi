#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 12: Contact List
#       Version: 2.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

with open('class_koi/code/shaine/python/data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)


headers = lines[0].split(', ')
# print(headers)

contacts = []

for i in range (1, len(lines)):
    full_entry  = {}
    for header in headers:
        info = lines[i].split(', ')
        entry = {header:info[headers.index(header)]}
        full_entry.update(entry)
    contacts.append(full_entry)

# print(contacts)


while True:
    user_input = input('Do you want to [c]reate, [r]etrieve, [u]pdate, [d]elete or [q]uit? ')
    
    # Create a record
    if user_input == 'c':
        new_entry = {}
    
        for header in headers:
            info = input(f'Enter {header}: ')
            entry = {header:info}
            new_entry.update(entry)
        contacts.append(new_entry)
        print(new_entry)
    
    # Retrieve a record
    elif user_input == 'r':
        retrieve = input('Enter a name: ')
        for contact in contacts:
            # print(contact)
            if contact['name'] == retrieve:
                print(contact)

    # Update a record
    elif user_input == 'u':
        name = input('Enter name: ')
        update = input('Enter number to update [1] name, [2] fruit or [3] color: ')
        if update == '1':
            for contact in contacts:
                if contact['name'] == name:
                    new_name = input('Enter new name: ')
                    contact['name'] = new_name
                    print(contact)

        if update == '2':
            for contact in contacts:
                if contact['name'] == name:
                    new_fruit = input('Enter new fruit: ')
                    contact['favorite fruit'] = new_fruit
                    print(contact)

        if update == '3':
            for contact in contacts:
                if contact['name'] == name:
                    new_color = input('Enter new color: ')
                    contact['favorite color'] = new_color
                    print(contact)
  
    # Delete a record
    elif user_input == 'd':
        name = input('Enter name: ')
        for contact in contacts:
                if contact['name'] == name:
                    contacts.remove(contact)
                    print(contacts)

    else:
        break













