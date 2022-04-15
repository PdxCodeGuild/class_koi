'''
Lab 11: Compute Automated Readability Index (ARI)

ARI formula: 4.71(characters/words) + 0.5(words/sentences) - 21.43
    -if the result is a decimal, always round up
    -if score goes above 14, the age and grade level should correspond to a score of 14
'''

import math

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

characters = 0
words = 1
sentences = 0
text_file = 'gettysburg-address.txt'

with open(text_file, 'r') as f: # test.txt is 12 words, 59 characters (no spaces), 68 characters (w spaces), 3 sentences, 3 lines.
    ARI_text = f.read()

# print(ARI_text)

for i in range(len(ARI_text)):
    if ARI_text[i].isalpha():
        characters += 1
    if ARI_text[i].isspace():
        words += 1
    if ARI_text[i] == '.' or ARI_text[i] == '!' or ARI_text[i] == '?':
        sentences += 1


ARI_score = math.ceil(4.71 * characters / words + 0.5 * words / sentences - 21.43)

if ARI_score > 14:
    ARI_score = 14

print(f"The ARI for {text_file} is {ARI_score}.")
print(f"This corresponds to a {ari_scale[ARI_score]['grade_level']} level of difficulty.")
print(f"Suitable for an average person {ari_scale[ARI_score]['ages']} years old.")
