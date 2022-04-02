'''
Lab 12: Contact List
- versions 1 - 3
- I only authenticated the initial inputs (c/r/u/d/'done').
- upload contacts.csv into git as well when you do the commit
'''

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n') # read the file into lines

contact_book_list = []
contact_book = []

def crud(user_entry): # VERSION 2: this and the while loop at the bottom are version 1
    if user_entry == 'c':
        create()
    elif user_entry == 'r':
        retrieve()
    elif user_entry == 'u':
        update()
    elif user_entry == 'd':
        delete()
    elif user_entry == 'done':
        done()

def back_to_list(list_of_dicts):
    final_contact_list = []
    for i in range(len(list_of_dicts)):
        final_contact_list.append(list(list_of_dicts[i].values()))
    return final_contact_list

def create():
    new_name = input('What is the name? ').lower()
    new_number = input('What is the number? ')
    new_job = input('What is the job? ').lower()
    contact_book.append({'name': new_name, 'number': new_number, 'job': new_job})

def retrieve():
    search_name = input('What is the name you are looking for? ').lower()
    for i in range(len(contact_book)):
        if search_name in contact_book[i]['name']:
            print(contact_book[i])

def update():
    update_name = input('What is the name of the record you would like to update? ').lower()
    update_key = input('What is the info you would like to update? (name, phone number, job?) ').lower()
    update_info = input(f"What is the new {update_key}? ").lower()
    for i in range(len(contact_book)):
        if update_name in contact_book[i]['name']:
            contact_book[i][update_key] = update_info
            print('updated.')

def delete():
    delete_name = input('What is the name of the record you would like to delete? ').lower()
    for i in range(len(contact_book)):
        if delete_name in contact_book[i]['name']:
            delete_index = contact_book.index(contact_book[i])
    contact_book.remove(contact_book[delete_index])
    print(f"{delete_name} deleted.")
    
def done(): # update csv file -> exit program
    final_list = back_to_list(contact_book) # VERSION 3 - write back to the csv
    with open('contacts.csv', 'w') as updated_contact_book: 
        # first access the dictionaries
        for i in range(len(final_list)):
            for j in range(len(final_list[i])):
                updated_contact_book.write(f'{final_list[i][j]}')
                if j < (len(final_list[i]) - 1): # i need to include this so it doesn't write a comma after the last value
                    updated_contact_book.write(',')
            if i < (len(final_list) - 1):
                updated_contact_book.write('\n')
    exit()

def back_to_list(list_of_dicts): # to write back to a csv I need a list of strings
    final_contact_list = []
    for i in range(len(list_of_dicts)):
        final_contact_list.append(list(list_of_dicts[i].values())) # .values() returns the values in the dict as a list
    return final_contact_list

for line in lines: # separate lines by commas
    temp_lines = line.split(',') # ['name', 'favorite fruit', 'favorite color']
    contact_book_list.append(temp_lines)

for n in range(len(contact_book_list)): # this is pretty much version 1
    contact_dict = {contact_book_list[0][0]: contact_book_list[n][0],
    contact_book_list[0][1]: contact_book_list[n][1],
    contact_book_list[0][2]: contact_book_list[n][2],
    }
    contact_book.append(contact_dict)

crud_list = ['c', 'r', 'u', 'd', 'done']

while True:
    user_entry = input("What would you like to do? (C/R/U/D/'done'?) ").lower()
    if user_entry in crud_list:
        crud(user_entry)
    else:
        print('not a valid entry.')
