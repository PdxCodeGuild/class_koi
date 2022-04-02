#----- Version 1 -----#
path_to_folder = './data/family_location.csv'

with open(path_to_folder, 'r') as file:
    lines = file.read().split('\n')

rows_list = []

for line in lines:
    rows_list.append(line.split(','))

key_list = rows_list.pop(0)

contact_list = []

for row in rows_list:
    contact_list.append({key_list[0]:row[0],key_list[1]:row[1],key_list[2]:row[2],key_list[3]:row[3]})

# print(lines)
# print('-'*72)
# print(rows_list)
# print('-'*72)
# print(key_list)
# print('-'*72)
# print(contact_list)

#----- Version 2 -----#

def create(contact_list,key_list):

    add_contact = {}

    for i, key in enumerate(key_list):
        add_contact[key] = input(f"\nWhat is your contact's {key_list[i]}? ")
    contact_list.append(add_contact)
    return (f'\nContact created: {add_contact}\n\n{contact_list}')

# print(create(contact_list,key_list))

def read(contact_list,key_list):
    
    key_string = '\n' + '\n'.join(key_list) + '\n'*2
    key_input = input(f"\nWhat would you like to search by? Choose from:{key_string}")
    contact_input = input("\nWhat is your search term? ")

    for contact in contact_list:
        if contact[key_input] == contact_input:
            return contact

# print(read(contact_list,key_list))


def update(contact_list,key_list):
    
    contact_output = read(contact_list,key_list)
    key_string = '\n' + '\n'.join(key_list) + '\n'*2
    update_key = input(f"\nWhat category would like to update?{key_string} ")
    update_value = input(f"\nwhat do you want to change {update_key} to? ")
    contact_output[update_key] = update_value
    return (f'\nContact updated to {contact_output}')

# print(update(contact_list,key_list))
    

def delete(contact_list,key_list):
    
    contact_delete = read(contact_list,key_list)
    delete_yes_no = input(f"\nDo you want to delete this contact, (y) or (n)? ")
    
    if delete_yes_no == 'y':
        contact_list.remove(contact_delete)
        return (f'\nContact deleted: {contact_delete}\n\n{contact_list}')
    else:
        print('\nNo deletions were made')

# print(delete(contact_list,key_list))

while True:
    
    user_input = input('''\nWelcome, to the Family Locator!
    Type "c" to create, "r" to read, "u" to update, "d" to delete or "q" to exit: ''')

    if user_input == 'q':
        print('\nGoodbye\n')
        break
    elif user_input == 'c':
        print(create(contact_list,key_list))
    elif user_input == 'r':
        print(read(contact_list,key_list))
    elif user_input == 'u':
        print(update(contact_list,key_list))
    elif user_input == 'd':
        print(delete(contact_list,key_list))
    
#----- Version 3 -----#

csv_output = []
csv_output.append(key_list)

for contact in contact_list:
    csv_output.append(list(contact.values()))

csv_output = [','.join(line) for line in csv_output]
csv_output = '\n'.join(csv_output)

with open(path_to_folder, 'w') as file:
    file.write(csv_output)