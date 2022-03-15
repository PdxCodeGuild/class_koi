'''
PDX Code Guild - Class Koi
Lab 01 - Unit Converter
Matt Walsh
'''

# dictionary containing units and conversion rates vs meters
converter = {
    'in':.0254,
    'ft':.3048,
    'yd':.9144,
    'mi':1609.34,
    'm':1,
    'km':1000
}

while True: # loop for validating length/distance entry
    distance = input('Please enter a length/distance to convert: ')
    try: # try converting entry to a float, prompt for re-entry if an error is caused
        distance = float(distance) 
        break
    except:
        print('I\'m sorry, that is not a valid entry. Please try again.')

while True: # loop for validating unit entry against dictionary
    start_unit = input('Please enter the unit of measurement for that length/distance (valid options are in, ft, yd, mi, m, & km): ')
    if start_unit in converter: # move on if unit is in dictionary
        break
    else: # prompt for re-entry if unit is not in dictionary
        print("This is not a valid unit of length/distance. Please try again.")

while True:# loop for validating unit entry against dictionary
    end_unit = input('Please enter the unit of measurement you would like to convert to (valid options are in, ft, yd, mi, m, & km): ')
    if end_unit in converter: # move on if unit is in dictionary
        break
    else: # prompt for re-entry if unit is not in dictionary
        print("This is not a valid unit of length/distance. Please try again.")

# display results
print(f'{distance} {start_unit} is equal to {distance * converter[start_unit] / converter[end_unit]} {end_unit}')