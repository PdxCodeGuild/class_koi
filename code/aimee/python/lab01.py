
units = {
    'feet':.3048,
    'miles':1609.34,
    'meters':1,
    'kilometers':1000,
    'yard':.9144,
    'inch':.0254
}

# ver 1 ---- #

# ask user for number of feet
measurement = input('Enter the distance: ')
# store the user's answer
meters = units['feet']
# convert to integer
measurement = int(measurement)
# convert to meters
# total = measurement * meters

# print(f'{measurement} ft is {total} m')

# ver 2 ---- # 

user_unit = input('Enter unit of measurement: ')
meters = units[user_unit]

total = measurement * meters

print(f'{measurement} {user_unit} ft is {round(total, 2)} m')

# ver 3 ---- #

# added support for yards and inches in dict above

# ver 4 ---- #

# started over with code - comment out everything above #
measurement = input('Enter the distance: ')
input_unit = input('Enter the unit of measurement: ')
output_unit = input('Enter the measurement you want to convert to: ')

# storing and converting to int
meters = units[input_unit]
measurement = int(measurement)

# convert user's input unit to meters
total = measurement * meters

# convert from meters to user's output unit
final_output = total / units[output_unit]

#result
print(f'{measurement} {input_unit} is {round(final_output, 2)} {output_unit}')
