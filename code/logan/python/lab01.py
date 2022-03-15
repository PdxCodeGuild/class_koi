## Did it with conditionals this time...much harder!  Note: no support for invalid input.
## Here is version 1:

# def feet_to_meters(x):
#     return int(x) * .3048

# distance_feet = input("\nGive me a distance in feet:  ")

# print(f"\n{distance_feet} ft is {feet_to_meters(distance_feet)}.")

## Here is version 2

# def feet_to_meters(x):
#     return int(x) * .3048

# def miles_to_meters(x):
#     return int(x) * 1609.34

# def kilometers_to_meters(x):
#     return int(x) * 1000

# distance_input = input("\nGive me a distance:  ")
# unit_input = input("\nWhat are the units?:  ")

# if unit_input == "ft":
#     print(f"\n{distance_input} {unit_input} is {feet_to_meters(distance_input)} m.")
# elif unit_input == "m":
#     print((f"\n{distance_input} {unit_input} is {(distance_input)} m."))
# elif unit_input == "km":
#     print(f"\n{distance_input} {unit_input} is {kilometers_to_meters(distance_input)} m.")
# elif unit_input == "mi":
#     print(f"\n{distance_input} {unit_input} is {miles_to_meters(distance_input)} m.")

# Here is version 3:

# def feet_to_meters(x):
#     return int(x) * .3048

# def miles_to_meters(x):
#     return int(x) * 1609.34

# def kilometers_to_meters(x):
#     return int(x) * 1000

# def yards_to_meters(x):
#     return int(x) * 0.9144

# def inches_to_meters(x):
#     return int(x) * 0.0254

# distance_input = input("\nGive me a distance:  ")
# unit_input = input("\nWhat are the units?:  ")

# if unit_input == "ft":
#     print(f"\n{distance_input} {unit_input} is {feet_to_meters(distance_input)} m.")
# elif unit_input == "m":
#     print((f"\n{distance_input} {unit_input} is {(distance_input)} m."))
# elif unit_input == "km":
#     print(f"\n{distance_input} {unit_input} is {kilometers_to_meters(distance_input)} m.")
# elif unit_input == "mi":
#     print(f"\n{distance_input} {unit_input} is {miles_to_meters(distance_input)} m.")
# elif unit_input == "yards" or unit_input == "yard":
#     print(f"\n{distance_input} {unit_input} is {yards_to_meters(distance_input)} m.")
# elif unit_input == "inches" or unit_input == "inch":
#     print(f"\n{distance_input} {unit_input} is {inches_to_meters(distance_input)} m.")

# Version 4:

def feet_to_meters(x):
    return int(x) * .3048

def miles_to_meters(x):
    return int(x) * 1609.34

def kilometers_to_meters(x):
    return int(x) * 1000

def yards_to_meters(x):
    return int(x) * 0.9144

def inches_to_meters(x):
    return int(x) * 0.0254

def meters_to_feet(x):
    return int(x) / .3048

def meters_to_miles(x):
    return int(x) / 1609.34

def meters_to_kilometers(x):
    return int(x) / 1000

def meters_to_yards(x):
    return int(x) / 0.9144

def meters_to_inches(x):
    return int(x) / 0.0254

value_in_meters = 0
distance_input = input("\nGive me a distance:  ")
unit_input = input("\nWhat are the units?:  ")
unit_conversion = input("\nWhat are the desired units?:  ")

if unit_input == "ft":
    value_in_meters = feet_to_meters(distance_input)
elif unit_input == "m":
    value_in_meters = int(distance_input)
elif unit_input == "km":
    value_in_meters = kilometers_to_meters(distance_input)
elif unit_input == "mi":
    value_in_meters = miles_to_meters(distance_input)
elif unit_input == "yards" or unit_input == "yard":
    value_in_meters = yards_to_meters(distance_input)
elif unit_input == "inches" or unit_input == "inch":
    value_in_meters = inches_to_meters(distance_input)

if unit_conversion == "ft":
    print(f"\n{distance_input} {unit_input} is {meters_to_feet(value_in_meters)} ft.")
elif unit_conversion == "m":
    print(f"\n{distance_input} {unit_input} is {value_in_meters} m.")
elif unit_conversion == "km":
    print(f"\n{distance_input} {unit_input} is {meters_to_kilometers(value_in_meters)} km.")
elif unit_conversion == "mi":
    print(f"\n{distance_input} {unit_input} is {meters_to_miles(value_in_meters)} mi.")
elif unit_conversion == "yard" or unit_conversion == "yards":
    print(f"\n{distance_input} {unit_input} is {meters_to_yards(value_in_meters)} yard/s.")
elif unit_conversion == "inch" or unit_conversion == "inches":
    print(f"\n{distance_input} {unit_input} is {meters_to_inches(value_in_meters)} inch/es.")    








