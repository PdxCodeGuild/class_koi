'''
PDX Code Guild - Class Koi
Optional Lab - Madlibs
Matt Walsh
'''

 
# Version 1
""" 
print('Let\'s make a story together. I\'ll provide the story, you fill in the details.')
adjective = input('Please enter an adjective: ').capitalize()
noun = input('Please enter a noun: ').lower()
animal = input('Please enter an animal: ').lower()
sound = input('Please enter a sound: ').upper()

print('\nThank you. Check out our story (which is more of an obnoxious song):\n\n')



print(adjective + ' Macdonald had a ' + noun + ', E-I-E-I-O')
print('and on that ' + noun + ' he had an ' + animal + ', E-I-E-I-O')
print('with a ' + sound + ' ' + sound + ' here')
print('and a ' + sound + ' ' + sound + ' there,')
print('here a ' + sound + ', there a ' + sound + ',')
print('everywhere a ' + sound + ' ' + sound + ',')
print(adjective + ' Macdonald had a ' + noun  + ', E-I-E-I-O.')
 """


# Version 2
""" 
import random

# dictionary to fill with user entry
words = {
    'noun':[],
    'plural noun':[],
    'verb':[],
    'verb ending in "ed"':[],
    'verb ending in "ing"':[],
    'adjective':[],
}

# dictionary defining how many of each type is needed for this madlib
this_madlib = {
    'noun':7,
    'plural noun':5,
    'verb':3,
    'verb ending in "ed"':1,
    'verb ending in "ing"':1,
    'adjective':5,
}

while True:
    print('Let\'s write the Declaration of Something together.')
    for type in this_madlib: # iterate through word types in this madlib
        # ask user to enter words, displaying number and type of words pulled from dictionary
        user_entry = input(f'Please enter {this_madlib[type]} {type if this_madlib[type] == 1 else type + "s"}{" separated by commas" if this_madlib[type] > 1 else ""}: ')
        words[type] = (user_entry.split(', ')) # convert user entry into list split at commas and insert into dictionary
        while len(words[type]) < this_madlib[type]: # if not enough words were entered, prompt for more
            # let user know how many more words to enter
            user_entry = input(f'You only entered {len(words[type])} {type if len(words[type]) == 1 else type + "s"}. Please enter {this_madlib[type] - len(words[type])} more: ')
            # split at commas and append to list in dictionary
            user_entry = user_entry.split(', ')
            for entry in user_entry:
                words[type].append(entry)
    for type in words: # shuffle words in each list in dictionary
        random.shuffle(words[type])

    # print results
    print(f'''
For better or worse, here's the Declaration of Something:


We hold these {words['plural noun'][0]} to be self-{words['adjective'][0]},
that all {words['plural noun'][1]} are created {words['adjective'][1]},
that they are {words['verb ending in "ed"'][0]} by their {words['noun'][0]} with certain {words['adjective'][2]} {words['plural noun'][2]},
that among these are {words['noun'][1]},
{words['noun'][2]} and the {words['verb'][0]} of {words['noun'][3]} -- That to secure these {words['plural noun'][2]},
{words['plural noun'][3]} are instituted among {words['plural noun'][1]},
{words['verb ending in "ing"'][0]} their {words['adjective'][3]} {words['plural noun'][4]} from the Consent of the {words['noun'][4]},
that whenever any Form of {words['noun'][5]} becomes {words['adjective'][4]} of these Ends,
it is the {words['noun'][6]} of the People to {words['verb'][1]} or to {words['verb'][2]} it...
    ''')
    break
 """


# Version 3

import random

# define madlib function
def madlib():
    # dictionary to fill with user entry
    words = {
        'noun':[],
        'plural noun':[],
        'verb':[],
        'verb ending in "ed"':[],
        'verb ending in "ing"':[],
        'adjective':[],
    }

    # dictionary defining how many of each type is needed for this madlib
    this_madlib = {
        'noun':7,
        'plural noun':5,
        'verb':3,
        'verb ending in "ed"':1,
        'verb ending in "ing"':1,
        'adjective':5,
    }

    while True:
        print('Let\'s write the Declaration of Something together.')
        for type in this_madlib: # iterate through word types in this madlib
            # ask user to enter words, displaying number and type of words pulled from dictionary
            user_entry = input(f'Please enter {this_madlib[type]} {type if this_madlib[type] == 1 else type + "s"}{" separated by commas" if this_madlib[type] > 1 else ""}: ')
            words[type] = (user_entry.split(', ')) # convert user entry into list split at commas and insert into dictionary
            while len(words[type]) < this_madlib[type]: # if not enough words were entered, prompt for more
                # let user know how many more words to enter
                user_entry = input(f'You only entered {len(words[type])} {type if len(words[type]) == 1 else type + "s"}. Please enter {this_madlib[type] - len(words[type])} more: ')
                # split at commas and append to list in dictionary
                user_entry = user_entry.split(', ')
                for entry in user_entry:
                    words[type].append(entry)
        for type in words: # shuffle words in each list in dictionary
            random.shuffle(words[type])

        # assign story to variable, then print
        story = (f'''
    For better or worse, here's the Declaration of Something:


    We hold these {words['plural noun'][0]} to be self-{words['adjective'][0]},
    that all {words['plural noun'][1]} are created {words['adjective'][1]},
    that they are {words['verb ending in "ed"'][0]} by their {words['noun'][0]} with certain {words['adjective'][2]} {words['plural noun'][2]},
    that among these are {words['noun'][1]},
    {words['noun'][2]} and the {words['verb'][0]} of {words['noun'][3]} -- That to secure these {words['plural noun'][2]},
    {words['plural noun'][3]} are instituted among {words['plural noun'][1]},
    {words['verb ending in "ing"'][0]} their {words['adjective'][3]} {words['plural noun'][4]} from the Consent of the {words['noun'][4]},
    that whenever any Form of {words['noun'][5]} becomes {words['adjective'][4]} of these Ends,
    it is the {words['noun'][6]} of the People to {words['verb'][1]} or to {words['verb'][2]} it...
        ''')
        print(story) # display results
        return

# assign story to variable for reuse while also calling function
story = madlib()



while True: # allow user to choose what happens next
    what_next = input('Would you like to start over or quit? Type "again", "start over", or "quit": ').lower()
    if what_next == 'again':
        print(story)
    elif what_next == 'start over':
        madlib()
    elif what_next == 'quit':
        break
    else:
        print('I didn\'t understand that.')