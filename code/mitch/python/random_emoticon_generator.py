# Random Emoticon Generator
# Version 1
# Mitch Chapman

import random


def random_emoticon_generator():
    eyes = [":", "8", ";", "=", "X", "B", "#:", ">:", "/:", "O:", "[", "@"]
    noses = ["-", "^"]
    mouths = [")", "(", "D", "/", "x", "P", "*", "S", "((", "))", "|", "B"]
    print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))


input("\nWelcome to the Random Emoticon Generator! Press 'enter' to generate a text emoticon.\n")
random_emoticon_generator()

while True:
    user_input = input("\nWould you like to generate another text emoticon? (Enter: 'Y' or 'n'): ").lower() or "y"
    print("")
    if user_input != "y" and user_input != 'n':
        print("Invalid entry. Please try again.")
    elif user_input == "y":
        random_emoticon_generator()
    elif user_input == "n":
        break

print("\nThank you for using the Random Emoticon Generator! Have a nice day!")














