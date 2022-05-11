user_score = input('Please enter the numeric grade (0-100): ')
# print(user_score, type(user_score))
user_score = int(user_score)
# print(user_score, type(user_score))

if user_score < 60:
    letter_grade = 'F'
elif user_score < 70:
    letter_grade = 'D'
elif user_score < 80:
    letter_grade = 'C'
elif user_score < 90:
    letter_grade = 'B'
else:
    letter_grade = 'A'

print(f'{user_score}% is a {letter_grade}')