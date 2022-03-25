'''
PDX Code Guild - Class Koi
Lab 11 - Compute ARI
Matt Walsh
'''


# import string functions for use in counting and splitting
from string import ascii_letters, digits

# variable for sentence-ending punctuation
sent_end = '.?!'

def count_sentences(inp):
    """
    Counts sentences in a string.
    """
    # split at periods
    period_split = inp.split('. ')
    # split at question marks 
    question_split = []
    for chunk in period_split:
        question_split.extend(chunk.split('? '))
    # split at exclamation points
    exclamation_split = []
    for chunk in question_split:
        exclamation_split.extend(chunk.split('! '))
    # return length of final split list
    return len(exclamation_split)

def count_words(inp):
    """
    Counts words in a string.
    """
    # split and return
    return len(inp.split())

def count_char(inp):
    """
    Counts characters in a string.
    """
    # assign variable to hold character count
    char_count = 0
    # iterate through every character and increment counter if letter or digit
    for char in inp:
        if char in ascii_letters or char in digits:
            char_count += 1
    # return counter
    return char_count

def ari(inp):
    """
    Uses above functions to determine ARI
    """
    # call functions and set variables
    characters = count_char(inp)
    words = count_words(inp)
    sentences = count_sentences(inp)
    # store float result
    result = (4.71 * (characters/words)) + (.5 * (words/sentences)) - 21.43
    # return results rounding up if needed
    if result > 14:
        return 14
    elif result % 1 == 0:
        return int(result)
    return int(result) + 1

# dictionary for equating ARI to ages and grade levels
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

# open and read file
with open('code\matt\python\lab11.txt', 'r') as f:
    contents = f.read()

# hold ari as variable to avoid calling multiple times
ari_score = ari(contents)

# display results
print(f"""
The ARI for lab11.txt (Dracula) is {ari_score}
This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari_score]['ages']} years old.
""")