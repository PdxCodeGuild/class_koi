import re

# Define ARI level parameters
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

# Compute the ARI for a given body of text loaded in from a file. You can find a .txt file to use at Project Gutenberg The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.

def ari():
    # Open file and read entire contents (My text file 'Ulysses' needs to be opened with utf-8)
    with open('text.txt', 'r', encoding='utf-8') as f:
        contents = f.read()

        # chars
        chars = []

        # iterate through each character. If character is an alphabet value, store in chars list.
        for i in contents:
            if(not(i.isalpha())):
                continue
            chars.append(i)

        # words
        # iterate through contents. If a ' ' or '\n' is found, it is a word and store in words as list
        words = re.split(' |\n', contents)

        # sentences
        # substitute line breaks and commas with spaces and store into sentences list if a period is encountered.
        sentences = re.sub('\n|, ', ' ', contents)
        sentences = sentences.split('.')
        
    # print(chars)
    # print(words)
    # print(sentences)

    '''
    number of characters divided by the number of words by 4.71
    4.71(chars/words)
    adding the number of words divided by the number of sentences multiplied by 0.5
    + 0.5(words/sentences)
    '''
    ari_score = int((4.71*(len(chars)/len(words))+(0.5*(len(words)/len(sentences)))))

    # print(ari_score)

    # The max ARI score is 14
    if(ari_score > 14):
        return 14
    
    return ari_scale

ari_score = ari()

print(f"This text received an ARI score of {ari_score}.\nSuitible for ages {ari_scale[ari_score].get('ages')}.\nGrade level is {ari_scale[ari_score].get('grade_level')} level")