from string import punctuation

with open('gatsby.txt', 'r', encoding = 'utf-8') as f:
    contents = f.read()

# Maybe in a future version I'll code a way to not make
# "Dr. T. J. Eckleburg" count as four sentences...

# Dictionary

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

# This preps the string to be sliced into sentences
# By making end punctuation something predictable

stringscrub = contents
stringscrub = stringscrub.replace("!", "~")
stringscrub = stringscrub.replace(".", "~")
stringscrub = stringscrub.replace("?", "~")
stringscrub = stringscrub.replace("\n", "")
sentence_list = stringscrub.split("~")
sentence_list.pop()

#Here is our sentence count:
sentence_count = len(sentence_list)

#Now let's get the number of words...

# This isn't getting all the punctuation, 
# some chars in the file must not be standard
# marks caught by punctuation from string.
# If I make a further version, I'll weed
# them out. 

for char in punctuation:
    stringscrub = stringscrub.replace(char, "#")
stringscrub = stringscrub.replace(" ", "#")


word_counter = 0
for i in range(len(stringscrub) -1):
    if (stringscrub[i] != "#") and (stringscrub[i +1] == "#"):
        word_counter += 1

# finally, let's count characters

stringscrub = stringscrub.replace("#", "")
char_counter = len(stringscrub)

ari_before_floor = (4.71 * (char_counter / word_counter)) + (.5 * (word_counter / sentence_count)) - 21.43
ari = ari_before_floor // 1

# Because there's no SUPER college level

if ari > 14:
    ari = 14

print(f"""
The ARI for gatsby.txt is {ari}.
This corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty
suitable for an average person {ari_scale[ari]["ages"]} years old.
""")





## Debugging
# print(stringscrub)
# print(word_counter)
# print(sentence_count)
# print(sentence_list)
# print(ari)