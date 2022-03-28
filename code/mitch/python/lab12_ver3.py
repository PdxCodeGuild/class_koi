# Lab 12: Contact List
# Version 3
# Mitch Chapman

filepath = 'code/mitch/python/data/'


# Opens the csv file for reading. It is read then split at the '\n' designation, resulting in the lines.
with open(filepath + 'weather_data.csv', 'r') as csv_file:
    lines = csv_file.read().split('\n')

# The first line is the headers or keys, these are split here by the comma.
keys = lines[0].split(',')

# Looping through the sencond line to the last line of data, they are split up by their commas and added to the values list.
values = []
for i in range (1, len(lines)):
    values.append(lines[i].split(','))

"""
A lot happens here. There are two for loops, one nested in the other. The first for loop occurs for each value in values.
The second for loop uses zip, which pairs up the key and value so that the day, temperature, and condition keys are assigned
to the appropriate value. The inner for loop runs 3 times because there are 3 of key in keys. The entire second for loop is 
enclosed in curly brackets so that produces a dicitonary for each day of weather. All of the data is in square brackets which
results in a list of dictionaries called 'weather_list'.
"""
weather_list = [{key:value for key, value in zip(keys, value)} for value in values]




def create():
    """Adds a new weather record for a city."""
    print("\nThis will add new weather data to the weather system.")
    city_to_add = input(f"Please enter the new city: ").title().strip()
    
    cities = []
    for weather_data in weather_list:
        cities.append(weather_data['City'])

    if city_to_add not in cities:
        new_values = []
        new_values.append(city_to_add)
        for key in keys[1:]:
            new_values.append(input(f"Please enter the new {key.lower()}: ").title().strip())
        data = {}
        for key, value in zip(keys, new_values):
            data[key] = value
        weather_list.append(data)
        print("Data was added, returning to main menu...")
    else:
        print(f"'{city_to_add}' was found in the current set of data. Please choose 'update' from the main menu.")

    

def retrieve():
    """Looks up and displays a weather record."""
    city_name = input("\nPlease enter the name of a city you would like to look up. ").title().strip()
    for weather_data in weather_list:
        if city_name in weather_data['City']:
            print(f"Here is the weather data for {weather_data['City']}:")
            for key in keys[1:]:
                print(f"{key}: {weather_data[key]}")



def update():
    """Pulls up a weather record and asks for temperature and/or condition updates."""
    city_to_update = input("\nPlease enter the city name you wish to update: ").title().strip()
    for weather_data in weather_list:
        if city_to_update in weather_data['City']:
            update_check = input(f"Are you sure you want to update the data for {weather_data['City']}? ('y' or 'n'): ").lower().strip()
            if update_check == 'y':
                for key in keys[1:]:
                    weather_data[key] = input(f"Enter the updated {key.lower()}: ").title().strip()
                print("Data was updated, returning to main menu...")
            else:
                print("Data was not updated, returning to main menu...")


def delete():
    """Finds a weather record and askes if you want to delete it (before deleting it)."""
    city_to_delete = input("\nPlease enter the city name you wish to delete: ").title().strip()
    for i, weather_data in enumerate(weather_list):
        if city_to_delete in weather_data['City']:
            delete_check = input(f"Are you sure you want to delete the data for {weather_data['City']}? ('y' or 'n'): ").lower().strip()
            if delete_check == 'y':
                weather_list.pop(i)
                print("Data was deleted, returning to main menu...")
            else:
                print("Data was not deleted, returning to main menu...")





print("""\n∙ Welcome to the weather records system. -------------------------------------------
--> If at any point the system returns you to the main menu, the data was not found.
--> The following are your options for what you can do with weather data points."""
)
while True:
    print("\n-------------------------------------MAIN MENU-------------------------------------")
    user_input = input("Would you like to [c]reate new, [r]etrieve, [u]pdate, [d]elete?, or [q]uit? ").lower().strip()
    if user_input not in ['c', 'r', 'u', 'd', 'q']:
        print("This is not a valid input, plese enter 'c', 'r', 'u', 'd', or 'q'.")
    if user_input == 'c':
        create()
    if user_input == 'r':
        retrieve()
    if user_input == 'u':
        update()
    if user_input == 'd':
        delete()

    if user_input == 'q':
        print("Thanks for using the weather records system. Any changes have been saved.")
        
        weather_data_strings = [",".join(keys)]

        for weather_data in weather_list:
            data = []
            for key in keys:
                data.append(weather_data[key])

            weather_data_strings.append(",".join(data))

        with open(filepath + 'weather_data.csv', 'w') as csv_file:
            csv_file.write("\n".join(weather_data_strings))
        
        break
