# Lab 12: Contact List
# Version 2
# Mitch Chapman

# Opens the csv file for reading. It is read then split at the '\n' designation, resulting in the lines.
with open('code/mitch/python/data/weather_data.csv', 'r') as csv_file:
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

print(f"weather: {weather_list}")


def create():
    """Adds a new weather record for a city."""
    ...


def retrieve():
    """Looks up and displays a weather record."""
    city_name = input("Please enter the name of a city you would like to look up. ").title()
    for weather_data in weather_list:
        if city_name in weather_data['City']:
            print(f"Here is the weather data for {weather_data['City']}:\nTemperature: {weather_data['Temperature']}\nCondition: {weather_data['Condition']}")



def update():
    """Pulls up a weather record and asks for temperature and/or condition updates."""
    ...
    

def delete():
    """Finds a weather record and askes if you want to delete it (before deleting it)."""
    ...










print("\nWelcome to the weather records system.")
print("The following are your options for what you can do with weather data points.")
while True:
    user_input = input("\nWould you like to  [c]reate new, [r]etrieve, [u]pdate, [d]elete?, or [q]uit? ").lower()
    if user_input not in ['c', 'r', 'u', 'd', 'q']:
        print("This is not a valid input, plese enter 'c', 'r', 'u', 'd', or 'q'.")
    if user_input == 'q':
        print("Thanks for using the weather records system.")
        break
    if user_input == 'c':
        create()
    if user_input == 'r':
        retrieve()
    if user_input == 'u':
        update()
    if user_input == 'd':
        delete()
        



