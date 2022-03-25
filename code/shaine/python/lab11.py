import string
import math

#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 11: Compute Automated Readability Index
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('class_koi/code/shaine/python/data/little_women.txt', mode='r', encoding='utf-8') as f:
    contents = f.read().split('\n')

# print(contents)

# converts content back to a string
string_content = str(contents)


# counts all of the sentences 
sentences = string_content.count('.') + string_content.count('!') + string_content.count('?') 

print(f'sentences: {sentences}')


# ''' I got the code snipit for remove_puncs from: 
#  https://stackoverflow.com/questions/16050952/how-to-remove-all-the-punctuation-in-a-string-python
# I understand that it runs a for loop over all the charaters 
# in string_content and uses .join() to replace/remove all puntuations 
# imported from the string module'''

remove_puncs = "".join(char for char in string_content if char not in string.punctuation)

# removes all the whitespace
split_words = remove_puncs.split()

# counts all the words in the list
words = len(split_words)

print(f'words: {words}')

# counts all the charaters of each word
charcters = 0
for word in split_words:
    charcters += len(word)

print(f'characters: {charcters}')

# calculates ARI
calc = 4.71*(charcters/words)+(words/sentences)-21.43

# rounds ARI up 
ari = math.ceil(calc)

# Scores greater than 14 should be presented as having the same age and grade level as scores of 14 
if ari > 14:
    ari = 14

output  = (f'''
The ARI for little_women.txt is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.''')

print(output)