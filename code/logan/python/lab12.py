## Lab 12
## Code

# Our empty list, to be filled with dictionaries
smashers = []

# Other variables

options = ""
options_list = ["0", "1", "2", "3", "4"]

######################################
# Here are all the necessary functions:


def create(dict_list, key_list):
# This is the function that creates a new character in the database.    
    name = input("Give me the character's name...").title()
    franchise = input("Give me the character's franchise...").title()
    up_b = input("Give me the character's up-b...").title()
    down_b = input("Give me the character's down-b...").title()
    side_b = input("Give me the character's side-b...").title()
    neutral_b = input("Give me the character's neutral-b...").title()
    char_as_list = [name, franchise, up_b, down_b, side_b, neutral_b] 
    new_dict = {}
    for i in range(0, len(key_list)):
        new_dict.update({key_list[i]:char_as_list[i]})
    dict_list.append(new_dict)
    print("\nCharacter created.")

def retrieve(dict_list):
# This is the function that retrieves a character's information as a dictionary.
    in_list = False
    name = input("\nWho do you want to look up?...")
    name = name.title()
    for dict in dict_list:
        if dict["Name"] == name:
            in_list = True
            print(dict)
            break

    if in_list == False:
        print("\nI'm sorry.  We haven't added that character yet!")

def uppdate(dict_list):
# Updates the data of an existing character in the database.
    in_list = False
    valid_responses = [1,2,3,4,5,6]
    att_list = ["Name","Franchise", "Up-B", "Down-B", "Side-B", "Neutral-B",]
    name = input("\nWho do you want to modify?...")
    name = name.title()
    for dict in dict_list:
        if dict["Name"] == name:
            in_list = True
            break
    if in_list == False:
        print("\nI'm sorry.  We haven't added that character yet!")
        return
    
    while True:
        try:
            att = input("\nInput the corresponding digit for the value you want to modify: \n\n1:Name\n2:Franchise\n3:Up-B\n4:Down-B\n5:Side-B\n6:Neutral-B\n\n...")
            att = int(att)
            if int(att) in valid_responses:
                break
        except:
            print("Invalid selction.  Please select again.")
    
    att_in = int(att) - 1
    update = input(f"\nWhat is the new {att_list[att_in]}?...")
    update = update.title()
    for dict in dict_list:
        if dict["Name"] == name:
            dict.update({att_list[att_in]:update})

def delete(dict_list):
# Deletes a character from the database.
    in_list = False
    name = input("\nWho do you want to remove?...")
    name = name.title()
    for dict in dict_list:
        if dict["Name"] == name:
            in_list = True
            dict_list.remove(dict)
            print("\nCharacter removed.")
            break 

    if in_list == False:
        print("\nI'm sorry.  That character is not in the game.")

def recompiler(key_list, smash_dict_list):
# This will recompile the data in a list
# that can be easily iterated upon to write
# the updated CSV
    recompiled_list = []
    recompiled_list.append(",".join(key_list))
    for smash_dict in smash_dict_list:
        char_values = []
        for i in range (0, len(smash_dict)):
            char_values.append(smash_dict[keys[i]])
        recompiled_list.append(",".join(char_values))
    return  recompiled_list

# Here end the functions
###########################

# Open the CSV

with open('smash.csv', 'r') as f:
    lines = f.read().split('\n')

# Harvest the keys as list items
keys = lines[0]
keys = keys.split(",")

# removes the keys line from imported list of CSVs
lines.pop(0)

# Makes dictionaries for each character, saves them in the list "smashers"
for line in lines:
    char_as_list = line.split(",")
    new_dict = {}
    for i in range(0, len(keys)):
        new_dict.update({keys[i]:char_as_list[i]})
    smashers.append(new_dict)

# The main menu REPL:

while options != "0":
    options = input(f"""
What would you like to do? (Input a digit below):
0 - Quit
1 - Create a character
2 - Look up a character
3 - Update a character
4 - Delete a character
...""")
    if options == "1":
        create(smashers, keys)
    elif options == "2":
        retrieve(smashers)
    elif options == "3":
        uppdate(smashers)
    elif options == "4":
        delete(smashers)
    elif options != "0":
        print("\nI'm sorry, that's not a valid response.")

# Recompiling data for CSV...

recompiled_data = recompiler(keys,smashers)

# Writing the new file...

with open('smashupdate.csv', 'w') as new_smash_sheet:
   for line in recompiled_data:
    new_smash_sheet.write(line + "\n")

#End

print("\nGoodbye!")


## Debugging

# create(smashers, keys)
# retrieve(smashers)
# uppdate(smashers)
# delete(smashers)
# print(lines)
# print(keys)
# print(",".join(keys))
# print(smashers)
# print(recompiler(keys,smashers))