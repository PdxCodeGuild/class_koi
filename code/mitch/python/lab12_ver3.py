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
    print("\nThis system will add new weather data to the weather system.")
    new_city = input("Please enter the new city name: ").title()
    new_temperature = input("Please enter the temperature for the city data: ")
    new_condition = input("Please enter the condition for the city data: ").title()
    data = {'City': new_city, 'Temperature': new_temperature, 'Condition': new_condition}
    weather_list.append(data)

    

def retrieve():
    """Looks up and displays a weather record."""
    city_name = input("Please enter the name of a city you would like to look up. ").title()
    for weather_data in weather_list:
        if city_name in weather_data['City']:
            print(f"Here is the weather data for {weather_data['City']}:\nTemperature: {weather_data['Temperature']}\nCondition: {weather_data['Condition']}")



def update():
    """Pulls up a weather record and asks for temperature and/or condition updates."""
    city_to_update = input("Please enter the city name you wish to update: ").title()
    for weather_data in weather_list:
        if city_to_update in weather_data['City']:
            weather_data['Temperature'] = input("Enter the updated temperature: ")
            weather_data['Condition'] = input("Enter the updated condition: ").title()

            


def delete():
    """Finds a weather record and askes if you want to delete it (before deleting it)."""
    city_to_delete = input("Please enter the city name you wish to update: ").title()
    for i, weather_data in enumerate(weather_list):
        if city_to_delete in weather_data['City']:
            delete_check = input(f"Are you sure you want to delete the data for {weather_data['City']}? ('y' or 'n'): ").lower()
            if delete_check == 'y':
                weather_list.pop(i)
            else:
                print("Data was not deleted, returning to main menu...")





print("""\nWelcome to the weather records system. ---------------------------------------------------
    If at any point the system returns you to the main menu, the data was not found.
    The following are your options for what you can do with weather data points."""
)
while True:
    user_input = input("\n------------MAIN MENU------------\nWould you like to [c]reate new, [r]etrieve, [u]pdate, [d]elete?, or [q]uit? ").lower()
    if user_input not in ['c', 'r', 'u', 'd', 'q', 'p']:
        print("This is not a valid input, plese enter 'p', 'c', 'r', 'u', 'd', or 'q'.")
    if user_input == 'c':
        create()
    if user_input == 'r':
        retrieve()
    if user_input == 'u':
        update()
    if user_input == 'd':
        delete()
    if user_input == 'p':
        print(f"weather: {weather_list}")

    if user_input == 'q':
        print("Thanks for using the weather records system. Any changes have been saved.")
        
        weather_data_strings = ["City,Temperature,Condition"]
        
        for weather_data in weather_list:
            data = []
            data.append(weather_data["City"])
            data.append(weather_data["Temperature"])
            data.append(weather_data["Condition"])
            weather_data_strings.append(",".join(data))

        
        with open(filepath + 'weather_data.csv', 'w') as csv_file:
            csv_file.write("\n".join(weather_data_strings))
        
        break
