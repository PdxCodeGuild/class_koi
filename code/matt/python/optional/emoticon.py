'''
PDX Code Guild - Class Koi
Optional Lab - Random Emoticon Generator
Matt Walsh
'''
 
# Version 1
""" 
from random import choice

# assign all parts to dictionaries and lists nested inside each other
ingredients = {
    'eyes': {
        'happy':[':','8','='],
        'sad':[':','>:'],
        'silly':[';','X','B',],
    },
    'noses': {
        'happy':['-','o'],
        'sad':['\'-','-'],
        'silly':['-','o','c','^'],
    },
    'mouths': {
        'happy':[')','D',']','}'],
        'sad':['(','[','{','|','/'],
        'silly':['D','3','O','P','>'],
    },
}

# define function to generate emoticons
def generate():
    emoticon = '' # empty string to store emoticon
    for part in ingredients: # iterate through face parts
        emoticon += choice(choice(list(ingredients[part].values()))) # choose a random part of each type from nested dictionaries/lists
    return emoticon

# display result
print(generate())
 """


# Version 2

from random import choice, randint

# assign all parts to dictionaries and lists nested inside each other
ingredients = {
    'eyes': {
        'happy':[':','8','='],
        'sad':[':','>:'],
        'silly':[';','X','B',],
    },
    'noses': {
        'happy':['-','o'],
        'sad':['\'-','-'],
        'silly':['-','o','c','^'],
    },
    'mouths': {
        'happy':[')','D',']','}'],
        'sad':['(','[','{','|','/'],
        'silly':['D','3','O','P','>'],
    },
}

# assign valid mood and nose choices to lists
mood_options = ['happy','sad','silly','any']
nose_options = ['yes', 'no', 'some']

# define function to generate emoticons
def generate(mood,nose):
    emoticon = '' # empty string to store emoticon
    if mood == 'any': # if user selected "any" mood, construct face ignoring mood
        for part in ingredients: # iterate through face parts
            if part == 'noses' and nose == 'no': # don't include noses if the user said "no"
                continue
            elif part == 'noses' and nose == 'some': # randomly include noses if the user said "some"
                if randint(1,10) % 2 == 0:
                    emoticon += choice(choice(list(ingredients[part].values())))
            else: # if the user said yes, always include a nose
                emoticon += choice(choice(list(ingredients[part].values())))
    else: # if the user selected a mood, construct face only from that mood
        for part in ingredients: # iterate through face parts
            if part == 'noses' and nose == 'no': # don't include noses if the user said "no"
                continue
            elif part == 'noses' and nose == 'some': # randomly include noses if the user said "some"
                if randint(1,10) % 2 == 0:
                    emoticon += choice(list(ingredients[part][mood]))
            else: # if the user said yes, always include a nose
                emoticon += choice(list(ingredients[part][mood]))
    # return result
    return emoticon

# loop for user options
while True:
    while True: # ask for number of noses and validate input
        num = input('How many emoticons do you want to generate? ')
        try:
            num = int(num)
            break
        except:
            print('That\'s not a valid number.')
    while True: # ask for mood and validate input
        mood = input('What mood do you want the faces to have? Happy, sad, silly, or any? ').lower()
        if mood in mood_options:
            break
        else:
            print('That\'s not a mood I recognize.')
    while True: # ask whether to include noses and validate input
        nose = input('Do you want the faces to have noses? Yes, no, or some? ').lower()
        if nose in nose_options:
            break
        else:
            print('That\'s not an option.')
    for x in range(num): # generate and display number of emoticons requested
        print(generate(mood,nose))
    # allow user to create more or quit
    what_next = input('Would you like to make some more? Yes or no. ').lower()
    if what_next == 'yes':
        continue
    else:
        break