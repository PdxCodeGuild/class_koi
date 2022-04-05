# Version 1 Lab 12
import random 
with open('something.csv','r') as csv_file:
        lines = csv_file.read().split("\n")
        
                      
headers = lines[0:1:]
key_list = headers[0]

values_only = lines[1::]
#print(values_only) 

keys_list = key_list.split(",")
#print(keys_list)


value_split = []
for value in values_only:
    value_split.append(value.split(","))
   # print (value_split)


info_list = []
# generates a dictionary and adds it to a list. 
for i, row in enumerate(value_split):
    dict = {}
    info_list.append(dict)
    for j, key in enumerate(keys_list):
        dict[key] = row[j]
#print(info_list)
""" Versoin 2
This is the Crud REPL portion
"""
# Creates a new record and appends it to list. 
def create_record(new_list):
    user_dict = {}
    username_input= input("What would you like your Username to be?")
    food_input = input("What is your favorite food? ")
    email_input = input("What is your email address: ")
    user_dict = dict.fromkeys(keys_list,)
    user_dict['userid'] = (f"dr{random.randint(1000,9999)}")
    user_dict[' username']= username_input
    user_dict[' favorite food'] = food_input
    user_dict[' e-mail'] = email_input
    info_list.append(user_dict)
    return info_list

# Retrieves user record aka dictionary via username search
def retrieve(info_list):
    user_input= input("What is the your username?")
    for i in info_list:
        for key, value in i.items():
            if user_input == value:
                return i
                
                
# Updates user info according to dict.key                
def update_info(info_list):    
    user_input = input("What is the username of the account you'd like to update? ")
    user_attribute = input ("What would you like to update? (username, favorite food or e-mail) ")
    user_answer = input ("Please give us updated information for matching field " )
    for i, row in enumerate (info_list):
        
        for key,value in row.items():
            
            if user_input == value:
                
                if user_attribute == key:
                    
                
                    row[user_attribute] = user_answer
            
                return info_list[i]
                    
# finds user record and removes            
def delete_record(info_list):           
        user_input = input("What is the username  for deletion?")
        for i, row in enumerate (info_list):
            for key, value in row.items():
                if user_input == value:
                    info_list.pop(i)
                    return info_list



# Testing of function functionality
print(create_record(info_list))
print(retrieve(info_list)) 
print(update_info(info_list))
print(delete_record(info_list))   

"""
Version 3, Write back to CSV
"""
with open('something.csv','w') as csv_file:
   output =",".join(keys_list)
csv_file.write (output)
for i in info_list:
    final =  ",".join(list(i.values()))
    csv_file.write(final) 
    
    

    