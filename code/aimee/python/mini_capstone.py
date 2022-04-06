'''
Python Mini Capstone

Pantry Helper
by Aimee Young
'''
from easygui import *

# CHANGELOG - changed from fresh_pantry to pantry_list to write file 


pantry_list = []

def write():
    '''writes to file'''
    # with open('/users/aimeeyoung/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f:    
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f: # windows
        f.write(pantry_list)


def flatten(pantry_list):
    '''flattens list of list into one list'''
    flat_pantry = []
    for elem in pantry_list:
        for item in elem:
            flat_pantry.append(item)
    return flat_pantry   

def delete_ingredient():
    '''deletes an ingredient from pantry list'''
    msg = "What would you like to delete?"
    title = 'Delete an item'
    choices = pantry_list # how to display pantry list as choices to delete?
    choice = choicebox(msg, title, choices)
    return choice # displays

def add_to_list():
    '''adds inputted ingredients to pantry list'''
def check_recipe():
    '''checks to see if any recipes match ingredients with pantry list'''
    
    



# Instantiate 
# pantry = Pantry()


# WELCOME BOX
# image = '/users/aimeeyoung/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png' # mac
image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png' # windows
msgbox(f"Welcome to Pantry Helper!\n We're here to help when you have a pantry (or fridge!) full of food, but don't know what to cook.\n The first step is inputting ingredigients that you have on hand.\n Let's get started!", ok_button='Let\'s get cooking!', image=image)

while True:
    # MENU BOX ----------------------------- #
    image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png'
    msg = 'What would you like to do?'
    choices = ['Input ingredigents','Delete ingredients','Find something to cook','See pantry','Exit']
    command = buttonbox(msg, image=image, choices=choices)
        
    # ADD INGREDIENTS --------------- #
    if command == choices[0]:
        # Enter ingredients; it's okay if user enters less than 5
        msg = 'Enter in your ingredients! You can add up to five at a time.'
        title = 'Pantry Helper'
        fieldnames = 'Ingredient 1','Ingredient 2','Ingredient 3','Ingredient 4','Ingredient 5',
        fieldvalues = []
        fieldvalues = multenterbox(msg, title, fieldnames)
        # add inputted values to pantry list
        pantry_list.append(fieldvalues)
        msgbox('Thank you! The ingredients have been added to your pantry list.', ok_button='Return to menu')
        
        # if user inputted more than 5 items, flatten out lists to one list
        if len(pantry_list) > 5: 
            flatten(pantry_list)
        
        # Convert pantry list to string
        ', '.join([str(x) for x in pantry_list])
        


        # empty values are added to list as ''; will need to remove those
        #pantry.pop('')
        
        

        # Ask user if they would like to add more
        # msg = 'Would you like to add more ingredients?'
        # yes_or_no = ['Yes','No']
        # add_more = buttonbox(msg, choices=choices)

        # need to figure out how to append this second list to first list? 
        # or, just have user return to menu to add more
        # if add_more == choices[0]:
        #     msg = 'Enter in your ingredients! You can add up to five at a time.'
        #     title = 'Pantry Helper'
        #     fieldnames = 'Ingredient 1','Ingredient 2','Ingredient 3','Ingredient 4','Ingredient 5',
        #     fieldvalues = multenterbox(msg, title, fieldnames)
        #     print(fieldvalues) # list index out of range line 46

    # DELETE INGREDIENTS ----------- #
    if command == choices[1]:
        flatten(pantry_list)
        delete_ingredient()


    # FIND SOMETHING TO COOK --------- #
    if command == choices[2]:    
        pass

    # SEE PANTRY -------------------- #   
    if command == choices[3]:        
        flatten(pantry_list)
        # print(pantry_list)
        # sorted_pantry = ','.join(map(str, pantry_list)) # TypeError: 'NoneType' object is not iterable
        msgbox = (pantry_list.sort()) # msgbox not showing but no error given
       
    # EXIT --------------------------- #
    if command == choices[4]:
        msgbox('Goodbye!', ok_button='Exit')
        break

print(pantry_list)
write()
    
    






































# with open('d:/documents/codeguildnotes/call-of-the-wild.txt', 'r', encoding='utf8') as f:
#     contents = f.read()

# welcome
# print(f'''Welcome to <Name>, a choose-your-fate story adventure. 
# When prompted, make your choice by entering in the corresponding number. 
# Make your decisions, and see if you live \n\nor die...\n''')
# time.sleep(2)
# your_name = input('Enter your name: ')
# # friends_name = input('Enter the name of a friend: ')
# time.sleep(1)

# # brief introduction
# print('-'*80 + '\n\n'  + 'HOW IT BEGINS') # (back.MAGENTA) colorama isn't working
# print('It\'s a cold Friday night in February, and you and your four friends have rented'\
#     ' an Airbnb for the weekend. The house is a beautiful, classic A-frame situated' \
#         ' on a remote road outside of Snoqualmie, Washington. There\'s fresh snow' \
#             ' on the ground, and you spend the first night cooking together and enjoying the view from the balcony.')

# print('...') + time.sleep(1)
# risk_counter = 0 

# while True:
#     print('\n\n2AM SATURDAY MORNING\n')
#     print('You wake up with a start, hearing the echo of a scream in the air. Or are you imagining it?'\
#         f' You tense in the darkness of the room you\'re sharing with your friend Taylor.'\
#             ' They are still sleeping soundly, softly snoring in their bed. It must\'ve been your '\
#                 'imagination, right? Or the several beers you had with dinner...')
#     ch_1_p1 = input('Do you...\n 1) Get out of bed and check on your other friends, or \n 2) Try to go back to sleep \n'\
#         'Make your choice: ')