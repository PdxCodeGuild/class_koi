print ('\nLab #1 Version 1, 2, 3, & 4\n')

print('\nWelcome to the Unit Converter\n')

user_distance = input('\nWhat is the distance?\n')

user_unit = input('What are the units?\n')

user_out_unit = input(f'What unit do you want {user_unit} converted to?\n')

user_distance = int(user_distance)

convert_to_mtr = {

    'in': .0254,
    'ft': .30448,
    'yrd': .9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

unit_scale = convert_to_mtr[user_unit]

unit_convert = user_distance * unit_scale

unit_scale_out = convert_to_mtr[user_out_unit]

mtr_convert_out = unit_convert / unit_scale_out

print(f'\n{user_distance} {user_unit} is {round(mtr_convert_out,2)} {user_out_unit}\n')
