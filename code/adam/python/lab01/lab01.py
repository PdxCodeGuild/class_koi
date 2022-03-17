# Lab 01 - Unit Converter
#-------------------------------------------------------------------
'''
# Version 1

# create a static conversion value variable
conversion_ft_to_m = 0.3048

# ask the user for the number in feet
feet_distance = input('Please enter the distance in feet: ')

# convert the input to int
feet_distance = int(feet_distance)

# convert the input feet distance into meters
output = feet_distance * conversion_ft_to_m

# print the converted value
print(f'{feet_distance} ft is {output} m')
'''
#------------------------------------------------------------------------
'''
# Version 2 - allow user to enter units: ft, mi, m, km then convert to meters

# create dictionary with keys as units and values as the conversions into meters
conversions = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000
}

# ask the user for the distance
distance = input('Please enter the distance: ')

# convert input string to integer
distance = int(distance)

#ask the user for the units
units = input('What are the units - ft, mi, m, km: ')

# get the conversion value of the user's units
conversion_value = conversions[units]

# perform conversion operation
output = distance * conversion_value

print(f'{distance} {units} is {output} m.')
'''
#-----------------------------------------------------------------------
'''
# Version 3 - add support for yards and inches to conversion module

# add in and yd to dictionary for the conversions into meters
conversions = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

# ask the user for the distance
distance = input('Please enter the distance: ')

# convert input string to integer
distance = int(distance)

#ask the user for the units
units = input('What are the units - in, ft, yd mi, m, km: ')

# get the conversion value of the user's units
conversion_value = conversions[units]

# perform conversion operation
output = distance * conversion_value

print(f'{distance} {units} is {output} m.')
'''
#---------------------------------------------------------------------------------

# Version 4

# create dictionary with keys as units and values as the conversions into meters
conversions = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

# ask the user for the distance
distance = input('What is the distance: ')

# convert input string to integer
distance = float(distance)

# ask the user for the units
units = input('What are the input units - in, ft, yd, mi, m, km: ')

# get the conversion value of the user's input units
conversion_value = conversions[units]

# perform conversion to meters operation
meter_conv = distance * conversion_value

# ask the user for the output units
output_units = input('What are the output units - in, ft, yd, mi, m, km: ')

# get the conversion value for the user's selected units
conv_value_2 = conversions[output_units]

# perform conversion from meters to user selected units
output = meter_conv / conv_value_2

# round output to nearest hundreth
output_rounded = round(output, 4)

print(f'{distance} {units} is {output_rounded} {output_units}.')
