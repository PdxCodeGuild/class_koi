'''
101 Lab 3: Unit Converter
Class Koi Lab 1: Unit Converter

This lab will involve writing a program that 
    allows the user to convert a number between units.

* no if / elif statements
 '''

units_dict = {
    'feet': 0.3048,
    'ft': 0.3048,
    'meters': 1,
    'm': 1,
    'mile': 1609.34,
    'miles': 1609.34,
    'mi': 1609.34,
    'kilometer': 1000,
    'km': 1000,
    'yard': 0.9144,
    'yd': 0.9144,
    'inch': 0.0254,
    'in': 0.0254
}

input_distance = float(input('What is the distance? '))
input_units = input('What are the input units? ')
output_units = input('What are the output units? ')

meters_distance = units_dict[input_units] * input_distance

output_distance = meters_distance / units_dict[output_units]

print(f'{input_distance} {input_units} is {round(output_distance, 4)} {output_units}.')

# 'units': ['foot', 'feet', 'ft', 'mile', 'miles', 'mi', 'meter', 'm', 'km', 'kilometers'],