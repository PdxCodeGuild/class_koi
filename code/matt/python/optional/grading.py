'''
PDX Code Guild - Class Koi
Optional Lab - Grading
Matt Walsh
'''

 
# Version 1
""" 
# loop to capture user input and validate
while True:
    grade_num = input('Please enter your grade score: ')
    try: # convert to integer if possible, then check if the score is within range
        grade_num = int(grade_num)
        if grade_num >= 0 and grade_num <= 100:
            break
        elif grade_num <= 0:
            print('Grade scores cannot be below 0.')
        else:
            print('Grade numbers cannot be above 100.')
    except: # if conversion to integer fails, show an error message and prompt for re-entry
        print('Grades must be entered as a numeric score between 0 and 100.')

# assign grade letter
if grade_num >= 90:
    grade_letter = 'A'
elif grade_num >= 80:
    grade_letter = 'B'
elif grade_num >= 70:
    grade_letter = 'C'
elif grade_num >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'

print(f'Your grade is {grade_letter}.') # display grade
"""

# Version 2

# loop to capture user input and validate
while True:
    grade_num = input('Please enter your grade score: ')
    try: # convert to integer if possible, then check if the score is within range
        grade_num = int(grade_num)
        if grade_num >= 0 and grade_num <= 100:
            break
        elif grade_num <= 0:
            print('Grade scores cannot be below 0.')
        else:
            print('Grade numbers cannot be above 100.')
    except: # if conversion to integer fails, show an error message and prompt for re-entry
        print('Grades must be entered as a numeric score between 0 and 100.')

# assign grade letter
if grade_num >= 90:
    grade_letter = 'A'
elif grade_num >= 80:
    grade_letter = 'B'
elif grade_num >= 70:
    grade_letter = 'C'
elif grade_num >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'

# add grade modifier to letter
if grade_num % 10 > 6 and grade_letter != 'F':
    grade_letter += '+'
elif grade_num % 10 < 3 and grade_letter != 'F':
    grade_letter += '-'

print(f'Your grade is {grade_letter}.') # display grade