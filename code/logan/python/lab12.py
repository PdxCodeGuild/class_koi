## Lab 12
## Code

# Our empty list, to be filled with dictionaries
smashers = []

# Open the CSV

with open('smash.csv', 'r') as f:
    lines = f.read().split('\n')

# Harvest the keys as list items
keys = lines[0]
keys = keys.split(",")

lines.pop(0)

# Make the dictionary
for line in lines:
    char_as_list = line.split(",")
    new_dict = {}
    for i in range(0, len(keys)):
        new_dict.update({keys[i]:char_as_list[i]})
    smashers.append(new_dict)

def create(dict_list, key_list):
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
    in_list = False
    name = input("\nWho do you want to look up?...")
    name = name.title()
    for dict in dict_list:
        if dict["Name"] == name:
            in_list = True
            print(dict)
            break

    if in_list == False:
        print("\nI'm sorry.  They haven't added that character to the game yet!")

def uppdate(dict_list):
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
        print("\nI'm sorry.  They haven't added that character to the game yet!")
        return

    att = input("\nInput the corresponding digit for the attribute you want to modify: \n\n1:Name\n2:Franchise\n3:Up-B\n4:Down-B\n5:Side-B\n6:Neutral-B\n\n...")
    att = int(att)
    if att in valid_responses:
        att_in = att - 1
        update = input(f"\nWhat is the new {att_list[att_in]}?...")
        update = update.title()
        for dict in dict_list:
            if dict["Name"] == name:
                dict.update({att_list[att_in]:update})

def delete(dict_list):
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

options = ""
options_list = ["0", "1", "2", "3", "4"]

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
    else:
        print("\nI'm sorry, that's not a valid response.")
        
print("\nGoodbye!")




    



## Debugging

# create(smashers, keys)
# retrieve(smashers)
# uppdate(smashers)
# delete(smashers)


# print(lines)
# print(keys)
print(smashers)

## Scraaaap

# # Make the dictionary
# for i in range (0, len(lines)):
#     new_dict = {}
#     for ii in range(0, len(keys)):
#         new_dict.update({lines[i]:keys[ii]})
#     smashers.append(new_dict)

# def delete(dict_list):
#     in_list = False
#     name = input("Who do you want to remove?...")
#     name = name.title()
#     for dict in dict_list:
#         if dict["Name"] == name:
#             in_list = True
#             dict_list.remove(dict)
#             print("Character removed.")
#             break 

#     if in_list == False:
#         print("I'm sorry.  They haven't added that character to the game yet!")

# while options != "0":
#     while True:
#         options = input(f"""
#         What would you like to do? (Input a digit below):
#         0 - Quit
#         1 - Create a character
#         2 - Look up a character
#         3 - Update a character
#         4 - Delete a character
#         ...""")
#         if options in options_list:
#             break
#         else:
#             print("\nI'm sorry, that's not a valid response.")
            
#         if options == "1":
#             create(smashers, keys)
#         elif options == "2":
#             retrieve(smashers)
#         elif options == "3":
#             uppdate(smashers)
#         elif options == "4":
#             delete(smashers)