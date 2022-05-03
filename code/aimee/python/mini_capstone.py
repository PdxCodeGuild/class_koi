'''
Python Mini Capstone

Pantry Helper
by Aimee Young
'''

from easygui import *
import requests

# FUNCTIONS ------------------------- #

def write(fresh_pantry):
    '''writes to file'''     
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'a') as f:     
        f.write(fresh_pantry)
 
def see_pantry():
    '''see a list of ingredients'''
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
            lines = f.read().split('\n')
            fresh_pantry = ', '.join([str(x) for x in lines])
    return msgbox(fresh_pantry)

def check_recipe(pantry_list):
    '''checks to see if any recipes match ingredients with pantry list'''
    with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
            lines = f.read().split('\n')
            fresh_pantry = ','.join([str(x) for x in lines])
    parameters = {
        'ingredients':fresh_pantry,
        'ranking':2, # minimize missing ingredients
        'ignorePantry':True, # ignore typical pantry items
        'limitLicense':True, 
    }
    
    endpoint = 'https://api.spoonacular.com/recipes/findByIngredients?apiKey=7ac571bc333b4b6686edfadbf2406ac4'
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get(endpoint, params=parameters, headers=headers)
    result = response.json()    
    title = [sub['title'] for sub in result]    
    recipes = ', \n'.join(title)    
    recipes_image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/recipes.png'
    msgbox(f'Here are some recipe ideas based on what you have in your pantry!\n\n {recipes}', image=recipes_image)      
    
# WELCOME BOX ----------------------------- #
image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png' 
msgbox(f"Welcome to Pantry Helper!\n We're here to help when you have a pantry (or fridge!) full of food, but don't know what to cook.\n The first step is inputting ingredigients that you have on hand.\n Let's get started!", ok_button='Let\'s get cooking!', image=image)

# REPL --------------------------------------- #

while True:
    # MENU BOX ----------------------------- #
    pantry_list = []
    image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry-helper.png'
    msg = 'What would you like to do?'
    choices = ['Input ingredigents','Delete ingredients','Find recipe ideas','See pantry','Exit']
    command = buttonbox(msg, image=image, choices=choices)
        
    # ADD INGREDIENTS --------------- #
    if command == choices[0]:
        msg = 'Enter in your ingredients! You can add up to five at a time.'
        title = 'Pantry Helper: Add Ingredients'
        fieldnames = 'Ingredient 1','Ingredient 2','Ingredient 3','Ingredient 4','Ingredient 5',        
        pantry_list = multenterbox(msg, title, fieldnames)
        # check if item is already in the list 
        with open('d:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
            for i in range(len(fieldnames)):
                if pantry_list[i].strip() in f.read():
                    msgbox(f'{pantry_list[i]} is already in your Pantry List!', ok_button='Oops!') 
                    pantry_list.remove(pantry_list[i])
                    break
                else:
                    continue
        added_image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/added_image.png'                
        msgbox('All done!', ok_button='Return to menu', image=added_image)    
        # Convert pantry list to string
        fresh_pantry = ','.join([str(x) for x in pantry_list])
        write(fresh_pantry + ',')  
     
    # DELETE INGREDIENTS ----------- #
    if command == choices[1]:
        # open file and get lines
        with open('d:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
            lines = f.read().split(',')
        msg = 'Input the ingredient you\'d like to delete.'
        title = 'Pantry Helper: Delete Ingredients'
        fieldnames = 'Enter:'.lower(),
        to_delete = multenterbox(msg, title, fieldnames)        
        x = ''.join(to_delete)
        
        if x in lines:            
            with open('d:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'w') as f:
                pantry_list = []
                lines.remove(x)
                pantry_list.append(lines)                
                fresh_pantry = ','.join([str(i) for i in lines])                
                f.write(fresh_pantry)            
            msgbox(f'{x} has been deleted!', ok_button='Woo!')
        elif x not in lines:
            msgbox('It doesn\'t look like that ingredient is in your pantry!', ok_button='Return to menu')

    # FIND SOMETHING TO COOK --------- #
    if command == choices[2]:    
        check_recipe(pantry_list)    

    # SEE PANTRY -------------------- #   
    if command == choices[3]:
        see_pantry()
       
    # EXIT --------------------------- #
    if command == choices[4]:
        goodbye_image = 'd:/documents/pdxcodeguild/class_koi/code/aimee/python/goodbye_image.png'
        msgbox('Goodbye!', ok_button='Exit', image=goodbye_image)
        break

# with open('D:/documents/pdxcodeguild/class_koi/code/aimee/python/pantry.txt', 'r') as f:
#             lines = f.read().split('\n')
#             fresh_pantry = ','.join([str(x) for x in lines])
            