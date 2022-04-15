# Version 1
path_to_data_folder = r'C:\Users\B\Desktop\PDXCode\class_koi\code\brandon\python\Lab11' # relative path

# if you have problems reading the text, give open the keyword argument encoding='utf-8'
with open(path_to_data_folder + '\sailing-alone-around-the-world.txt', 'r', encoding='utf-8') as f:
  
    contents = f.read()

translator = str.maketrans('', '', '#' and '_' and '*' and '[' and ']' and '-' and '"' )
paragraph_without_symbols = contents.translate(translator).lower()

chars = len(paragraph_without_symbols)
words = len(paragraph_without_symbols.split())
sentances = paragraph_without_symbols.find('.') + paragraph_without_symbols.find('!') + paragraph_without_symbols.find('?')

print(words, 'words')
print(chars, 'characters')
print(sentances, 'sentances')
math = 0.0

# math
math = 4.71*(chars/words) + .5*(words/sentances) - 21.43

maths = round(math, 0)
if maths > 14:
    maths = 14
print(math, 'ARI not rounded')
print(maths, 'ARI rounded')

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
    14: {'ages': '18-22', 'grade_level':      'College'},
}

x = ari_scale[maths]
ages = x['ages']
grade_level = x['grade_level']

print(f'The ARI for sailing-alone-around-the-world.txt is {maths}. This corresponds to a {grade_level} Grade level of difficulty that is suitable for an average person {ages} years old.')
