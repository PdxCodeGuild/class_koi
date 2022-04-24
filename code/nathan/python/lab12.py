'''
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.
'''

# this function retrieves the headers of the csv file and returns them as a list
def get_headers():
    # read the first line of the csv and split at ','s
    with open('contacts.csv') as file:
        lines = file.read().split('\n')
        headers = lines[0]

    headers = headers.split(',')

    return headers

# reads the csv and creates a list of dictionaries for each entry respective to the header
def contacts_list(headers):
    temp_list = [] # a placeholder for the csv lines
    new_list = [] # list of dictionaries

    with open('contacts.csv') as file:
        lines = file.read().split('\n')

        for i in range(1, len(lines)):
            #store csv contents into a list starting after headers
            temp_list.append(lines[i].split(','))
        
        # match the header as a key with temp_list as the value and store into new_list as a dictionary
        for i in range(len(temp_list)):
            new_dict = {}
            for j in range(len(headers)):
                new_dict.update({headers[j]:temp_list[i][j]})
            new_list.append(new_dict)

        print(new_list)

    return new_list

# CRUD and REPL function that takes the current contacts list and headers.
def crud_repl(headers, contacts_list):

    # creates a new item for list. returns item
    def create_record():
        user_dict = {}

        for header in headers:
            user_input = input("Please enter the " + header + ": ")
            user_dict.update({header:user_input})

        print(user_dict)

        return user_dict

    repl_flag = 'y' # flag to repeat while loop

    while(repl_flag == 'y'):
        success_flag = 0 # validates successful CRUD operation

        # sends user to appropriate if-statement based on input
        user_choice = int(input("""What would you like to do?
        1. Create a record
        2. Retrieve a record
        3. Update a record
        4. Delete a record
        5. Exit
        Please enter an option (1-5): """))

        # create a record
        if(user_choice == 1):
            contacts_list.append(create_record())
            print(contacts_list)

        # retrieve a record
        elif(user_choice == 2):
            user_input = input("Who's contact would you like to retrieve? ")
            
            # iterate through list to match name
            for i in contacts_list:
                if(i.get('name') == user_input):
                    print(i)
                    success_flag = 1
                    break

            # if the end of the list was reached, user doesn't exist
            if(not(success_flag)): # success_flag wasn't triggered
                print("User doesn't exist")
        
        # update a record
        elif(user_choice == 3):
            user_input = input("Who's contact would you like to update? ")

            # iterate through list to match name
            for i in range(len(contacts_list)):
                if(contacts_list[i].get('name') == user_input):
                    contacts_list[i] = create_record()
                    print(contacts_list)
                    success_flag = 1
                    break
            
            # if the end of the list was reached, user doesn't exist
            if(not(success_flag)): # success_flag wasn't triggered
                print("User doesn't exist")
        
        # delete a record
        elif(user_choice == 4):
            user_input = input("Who's contact would you like to delete? ")

            # iterate through list to match name
            for i in contacts_list:
                if(i.get('name') == user_input):
                    contacts_list.remove(i)
                    print(contacts_list)
                    success_flag = 1
                    break
            
            # if the end of the list was reached, user doesn't exist
            if(not(success_flag)): # success_flag wasn't triggered
                print("User doesn't exist")

        # exit
        elif(user_choice == 5):
            break
        
        # input validation
        else:
            print("Invalid Input! Please enter 1-5!")
        
        repl_flag = input("Do you want to do something else? (y/n): ")

        # input validation
        while(repl_flag != 'y' and repl_flag != 'n'):
            print("Invalid Input!  Please enter 'y' or 'n': ")
            repl_flag = input("Do you want to do something else? (y/n): ").lower()
        
    return contacts_list

# writes new list to a new csv file
def write_file(headers, contacts_list):
    to_csv = []
    revert_headers = ','.join(headers)
    for i in contacts_list:
        temp_list = []
        for header in headers:
            temp_list.append(i[header])
        temp_list = ','.join(temp_list)
        to_csv.append(temp_list)
    to_csv = '\n'.join(to_csv)

    with open('new_contacts.csv', 'w') as file:
        file.write(to_csv)

    print(to_csv)
            
        


headers = get_headers()
contacts_list = contacts_list(headers)
contacts_list = crud_repl(headers, contacts_list)
print(contacts_list)
write_file(headers, contacts_list)
