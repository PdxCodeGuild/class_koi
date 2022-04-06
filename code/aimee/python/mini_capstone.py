'''
Python Mini Capstone

Pantry Helper
by Aimee Young
'''
from easygui import *
import requests

# CHANGELOG 4/6 - 

# FUNCTIONS ------------------------- #

def write(fresh_pantry):
    '''writes to file'''
    # with open('/users/aimeeyoung/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f:    
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'a') as f: # windows       
        f.write(fresh_pantry)
     

def check():
    pass

def delete_ingredient():
    '''deletes an ingredient from pantry list'''
    # msg = "What would you like to delete?"
    # title = 'Delete an item'
    # # will need to read/write pantry.txt
    # with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f:
    #     f.write(fresh_pantry)
    # choices = fresh_pantry # NameError: name 'fresh_pantry' is not defined
    # choice = choicebox(msg, title, choices)
   

def check_recipe():
    '''checks to see if any recipes match ingredients with pantry list'''
    response = requests.get('https://api.spoonacular.com/recipes/findByIngredients&apiKey=7ac571bc333b4b6686edfadbf2406ac4', headers = {'content-type': 'application/json'})
    result = response.json()
    print(result)
    
# WELCOME BOX ----------------------------- #
# image = '/users/aimeeyoung/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png' # mac
image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png' # windows
msgbox(f"Welcome to Pantry Helper!\n We're here to help when you have a pantry (or fridge!) full of food, but don't know what to cook.\n The first step is inputting ingredigients that you have on hand.\n Let's get started!", ok_button='Let\'s get cooking!', image=image)

# REPL --------------------------------------- #
while True:
    # MENU BOX ----------------------------- #
    pantry_list = []
    image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png'
    msg = 'What would you like to do?'
    choices = ['Input ingredigents','Delete ingredients','Find something to cook','See pantry','Exit']
    command = buttonbox(msg, image=image, choices=choices)
        
    # ADD INGREDIENTS --------------- #
    if command == choices[0]:
        msg = 'Enter in your ingredients! You can add up to five at a time.'
        title = 'Pantry Helper: Add Ingredients'
        fieldnames = 'Ingredient 1','Ingredient 2','Ingredient 3','Ingredient 4','Ingredient 5',
        # fieldvalues = []
        pantry_list = multenterbox(msg, title, fieldnames)
        # check if item is already in the list 
        f = open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w')
        for i in range(len(fieldnames)):
            if pantry_list[i].strip() in f.read():
                msgbox(f'{pantry_list[i]} is already in your Pantry List!', ok_button='Oops!') # gave weird value if more than 1 ingredient inputted
                pantry_list.remove(pantry_list[i])
                break # doesn't work if you enter in more than 1 duplicate value
            else:
                continue
        
                
        msgbox('Thank you! The ingredients have been added to your pantry list.', ok_button='Return to menu')

        # Convert pantry list to string
        fresh_pantry = ','.join([str(x) for x in pantry_list])
        # print(fresh_pantry)
        write(fresh_pantry + ',')
        
     
    # DELETE INGREDIENTS ----------- #
    if command == choices[1]:
        msg = 'Input the ingredient you\'d like to delete.'
        title = 'Pantry Helper: Delete Ingredients'
        fieldnames = 'What do you want to delete?'
        to_delete = multenterbox(msg, title, fieldnames)
        f = open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w')
        for i in range(len(fieldnames)):
            if to_delete[i].strip() in f.read():
                msgbox(f'{pantry_list[i]} is already in your Pantry List!', ok_button='Oops!') # gave weird value if more than 1 ingredient inputted
                pantry_list.remove(pantry_list[i])
                break # doesn't work if you enter in more than 1 duplicate value
            else:
                continue


    # FIND SOMETHING TO COOK --------- #
    if command == choices[2]:    
        pass

    # SEE PANTRY -------------------- #   
    if command == choices[3]:
        with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
            lines = f.read().split('\n')
        msgbox(lines)
        
       
    # EXIT --------------------------- #
    if command == choices[4]:
        msgbox('Goodbye!', ok_button='Exit') # TypeError: 'list' object is not callable
        break

# choicebox not working for this
#  fresh_pantry = ','.join([str(x) for x in pantry_list])
#         msg = "What would you like to delete?"
#         title = 'Delete an item'
#         with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f:
#             f.write(fresh_pantry)
#         choices = fresh_pantry # NameError: name 'fresh_pantry' is not defined
#         choice = choicebox(msg, title, choices)