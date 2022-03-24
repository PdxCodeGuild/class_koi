#Version 1

unit_converter = {
    #Converts to meters
    "ft": 0.3048,
}

unit_input = input("Please enter a unit to convert to meters. Please choose from ft, mi, m, km, yards, inches. ");
number_input = input(f'How many {unit_input} would you like to convert? ');
final_num = int(number_input);

if unit_input == "ft":
    final_calc = final_num * unit_converter["ft"];
    print(f'{number_input}{unit_input} is {final_calc} meters');





# Version 2

unit_converter = {
    #Converts to meters
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
}

unit_input = input("Please enter a unit to convert to meters. Please choose from ft, mi, m, km, yards, inches. ");
number_input = input(int(f'How many {unit_input} would you like to convert? '));
final_num = int(number_input);

if unit_input == "ft":
    final_calc = final_num * unit_converter["ft"];
    print(final_calc);

elif unit_input == "mi":
    final_calc = final_num * unit_converter["mi"];
    print(final_calc);

elif unit_input == "m":
    final_calc = final_num * unit_converter["m"];
    print(final_calc);

elif unit_input == "km":
    final_calc = final_num * unit_converter["km"];
    print(final_calc);




# Version 3

unit_converter = {
    #Converts to meters
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yards": 0.9144,
    "inches": 0.0254
}

unit_input = input("Please enter a unit to convert to meters. Please choose from ft, mi, m, km, yards, inches. ");
number_input = input(int(f'How many {unit_input} would you like to convert? '));
final_num = int(number_input);


if unit_input == "ft":
    final_calc = final_num * unit_converter["ft"];
    print(final_calc);

elif unit_input == "mi":
    final_calc = final_num * unit_converter["mi"];
    print(final_calc);

elif unit_input == "m":
    final_calc = final_num * unit_converter["m"];
    print(final_calc);

elif unit_input == "km":
    final_calc = final_num * unit_converter["km"];
    print(final_calc);

elif unit_input == "yards":
    final_calc = final_num * unit_converter["yards"];
    print(final_calc);   

elif unit_input == "inches":
    final_calc = final_num * unit_converter["inches"];
    print(final_calc);



# Version 4

unit_converter = {
    #Converts to meters
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
}
distance_input = input(int('What is the distance?'));
unit_input = input("Please enter a unit to convert from. Please choose from ft, mi, m, km, yards, inches. ");
unit_output = input("Please enter a unit to convert to. Please choose from ft, mi, m, km, yards, inches. ");


if unit_input == "ft":
    final_calc = number_input * unit_converter["ft"];
    print(final_calc * 3.28);

elif unit_input == "mi":
    final_calc = number_input * unit_converter["mi"];
    print(final_calc * 6.21);

elif unit_input == "m":
    final_calc = number_input * unit_converter["m"];
    print(final_calc * 1);

elif unit_input == "km":
    final_calc = number_input * unit_converter["inches"];
    print(final_calc * .001);
