# Lab 11 - Compute Automated Readability Index
import string
punct = string.punctuation

# create path to text file
path_to_file = 'data/alice_in_wonderland.txt'

with open(path_to_file, 'r', encoding='utf-8') as f:
    
    contents = f.read()

# word count by counting spaces
# spaces_count = 0
# for i in contents:
#     if i == ' ':
#         spaces_count += 1
# print(f'word count by counting spaces: {spaces_count}')

# get word count of book
words_list = contents.split()
num_of_words = len(words_list)
print(f'word count spliting by space: {num_of_words}')

# sentence count of book
sent_punct_count = 0
for i in contents:
    if i == '!' or i == '?' or i == '.':
        sent_punct_count += 1
print(f'sentence count by !-.-?: {sent_punct_count}')

# length of characters in book
character_count = 0
for i in contents:
    if i.isalpha:
        character_count += 1
print(f'total amount of character: {character_count}')

ari = (4.71 * character_count / num_of_words) + (0.5 * num_of_words / sent_punct_count) - 21.43

ari_rounded = (round(ari + 0.5))

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

