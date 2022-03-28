import re
import math

path_to_data_folder = 'count_monte_cristo.txt'

with open(path_to_data_folder, 'r', encoding='utf-8') as f:
    contents = f.read()

def ari(contents):
    no_dash = contents.replace('-',' ')
    list_sentences = re.split('[.?!]', contents)
    list_words = no_dash.split(' ')
    list_char = re.findall(r'[A-Za-z0-9]',contents)
    sentences = len(list_sentences)
    words = len(list_words)
    char = len(list_char)
    ari_score = math.ceil(4.74 * (char/words) + .5 * (words/sentences) - 21.43)
    return ari_score

ari_scale = {
     
     1:{'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2:{'ages':   '6-7', 'grade_level':    '1st Grade'},
     3:{'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4:{'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5:{'ages':  '9-10', 'grade_level':    '4th Grade'},
     6:{'ages': '10-11', 'grade_level':    '5th Grade'},
     7:{'ages': '11-12', 'grade_level':    '6th Grade'},
     8:{'ages': '12-13', 'grade_level':    '7th Grade'},
     9:{'ages': '13-14', 'grade_level':    '8th Grade'},
    10:{'ages': '14-15', 'grade_level':    '9th Grade'},
    11:{'ages': '15-16', 'grade_level':   '10th Grade'},
    12:{'ages': '16-17', 'grade_level':   '11th grade'},
    13:{'ages': '17-18', 'grade_level':   '12th grade'},
    14:{'ages': '18-22', 'grade_level':      'College'},
    }

ari_result = ari(contents)
ari_output = ari_scale[ari_result]
ari_ages = ari_output['ages']
ari_grade = ari_output['grade_level']
# print(ari_output)

print('-'*72)
print(f'\nThe ARI for {f.name} is {ari_result}.')
print(f'This corresponds to a {ari_grade} level of difficulty')
print(f'that is suitable for an average person of {ari_ages} years old.\n')
print('-'*72)
