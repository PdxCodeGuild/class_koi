#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 1: Unit Converter 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

# Version  1
#Ask the user for the number of feet, and print out the equivalent distance in meters.

# feet  = int(input('what is the distance in feet? '))

# meter = round(feet*0.3048, 4)

# print(f'{feet} ft is {meter} m')

#  Version 2
# Allow the user to also enter the units. 
# Then depending on the units, convert the distance into meters. 
# The units we'll allow are feet, miles, meters, and kilometers.


# distance = int(input('what is the distance? '))

# unit  = input('what are the units? (ft, mi, m or km) ')

# if unit  == 'ft':
#     conversion = round(distance*0.3048, 4)
# elif unit == 'mi':
#     conversion = round(distance*1609.34, 4)
# elif unit == 'm':
#     conversion = round(distance*1, 4)
# elif unit == 'km':
#     conversion = round(distance*1000, 4)

# print(f'{distance} {unit} is {conversion} m')


# Version 3
# Add support for yards, and inches.

# distance = int(input('what is the distance? '))

# unit  = input('what are the units? (ft, mi, m, km, yd, or in) ')

# if unit  == 'ft':
#     conversion = round(distance*0.3048, 4)
# elif unit == 'mi':
#     conversion = round(distance*1609.34, 4)
# elif unit == 'm':
#     conversion = round(distance*1, 4)
# elif unit == 'km':
#     conversion = round(distance*1000, 4)
# elif unit == 'yd':
#     conversion = round(distance*0.9144, 4)
# elif unit == 'in':
#     conversion = round(distance*0.0254, 4)

# print(f'{distance} {unit} is {conversion} m')


# Version 4
# Now we'll ask the user for the distance, the starting units, and the units to convert to.

#created dictionary of all conversion values
convert_dict = {'m':1, 'ft':0.3048, 'mi':1609.34, 'km':1000, 'yd':0.9144, 'in':0.0254}

#inputs needed from user
distance = int(input('what is the distance? '))

input_units = input('what are the input units? (ft, mi, m, km, yd, or in) ')

output_units = input('what are the output units? ')


#convert any unit to meters, 

meter_convert = distance * convert_dict[input_units]


# #then convert the distance in meters to any other unit.

other_convert = meter_convert / convert_dict[output_units]

total = round(other_convert, 4)

print(f'{distance} {input_units} is {total} {output_units}')