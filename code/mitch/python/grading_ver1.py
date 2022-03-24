# Optional Lab 'Grading' - Version 1
# Mitch Chapman


while True:
    try:
        numeric_grade = int(input("\nPlease enter the percentage value representing the grade (0-100): \n"))
        break
    except ValueError:
        print("Please input integer only...")
        continue 


if 90 <= numeric_grade:
    print("The letter grade is:'A'")
elif 80 <= numeric_grade <= 89:
    print("The letter grade is:'B'")
elif 70 <= numeric_grade <= 79:
    print("The letter grade is:'C'")
elif 60 <= numeric_grade <= 69:
    print("The letter grade is:'D'")
else:
    print("The letter grade is:'F'")















