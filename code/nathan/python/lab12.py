'''
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.
'''

def get_headers():
    with open('contacts.csv') as file:
        lines = file.read().split('\n')
        headers = lines[0]
    headers = headers.split(',')
    return headers

def contacts_list(headers):
    temp_list = []
    new_list = []
    with open('contacts.csv') as file:
        lines = file.read().split('\n')

        for i in range(1, len(lines)):
            temp_list.append(lines[i].split(','))
        for i in range(len(temp_list)):
            new_dict = {}
            for j in range(len(headers)):
                new_dict.update({headers[j]:temp_list[i][j]})
            new_list.append(new_dict)

        print(new_list)
    return new_list

def crud_repl(headers, contacts_list):

    def create_record():
        user_dict = {}
        for header in headers:
            user_input = input("Please enter the " + header + ": ")
            user_dict.update({header:user_input})
        print(user_dict)
        return user_dict

    repl_flag = 'y'
    while(repl_flag == 'y'):
        success_flag = 0

        user_choice = int(input("""What would you like to do?
        1. Create a record
        2. Retrieve a record
        3. Update a record
        4. Delete a record
        5. Exit
        Please enter an option (1-5): """))

        if(user_choice == 1):
            contacts_list.append(create_record())
            print(contacts_list)


        elif(user_choice == 2):
            user_input = input("Who's contact would you like to retrieve? ")
            for i in contacts_list:
                if(i.get('name') == user_input):
                    print(i)
                    success_flag = 1
                    break
            if(not(success_flag)):
                print("User doesn't exist")
        
        elif(user_choice == 3):
            user_input = input("Who's contact would you like to update? ")
            for i in range(len(contacts_list)):
                if(contacts_list[i].get('name') == user_input):
                    contacts_list[i] = create_record()
                    print(contacts_list)
                    success_flag = 1
                    break
            if(not(success_flag)):
                print("User doesn't exist")
        
        elif(user_choice == 4):
            user_input = input("Who's contact would you like to delete? ")
            for i in contacts_list:
                if(i.get('name') == user_input):
                    contacts_list.remove(i)
                    print(contacts_list)
                    success_flag = 1
                    break
            if(not(success_flag)):
                print("User doesn't exist")

        elif(user_choice == 5):
            break
        
        else:
            print("Invalid Input! Please enter 1-5!")
        
        repl_flag = input("Do you want to do something else? (y/n): ")
        while(repl_flag != 'y' and repl_flag != 'n'):
            print("Invalid Input!  Please enter 'y' or 'n': ")
            repl_flag = input("Do you want to do something else? (y/n): ").lower()
        
    return contacts_list

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
