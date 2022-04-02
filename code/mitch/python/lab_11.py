# Lab 11: Compute Automated Readability Index
# Mitch Chapman

from string import punctuation
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

filepath = "code/mitch/python/data/"
filename = "the_great_gatsby.txt"

with open(filepath + filename, "r", encoding="utf-8") as file:    ### (, encoding="utf-8") add this to 'with open' if there is an encoding error
    contents = file.read()
    title = file.fileno



# Eliminates the punctuation, makes all words lowercase, and splits the words into a list, resulting in a list of the words which is counted.
translator = str.maketrans("", "", punctuation)
contents_list_without_punctuation = contents.translate(translator).lower().split()
words = len(contents_list_without_punctuation)


# Counts the number of characters in the book by looping through the characters in the words list.
characters = 0
for word in contents_list_without_punctuation:
    for char in word:
        characters += 1


# Counts the number of sentances by counting the number of periods in the book. (this is an estimate)
sentances = contents.count(".")


# Calculates the ARI score and rounds up to the next whole number.
ari = math.ceil((4.71 * (characters / words)) + (0.5 * (words / sentances)) - 21.43)


# If ARI score is beyond what the dictionary looks for it sets the score to 14.
if ari > 14:
    ari = 14


print()
print("-"*60)
print(f"""\nThe ARI for {filename} is {ari}.
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.\n"""
)
print("-"*60)








