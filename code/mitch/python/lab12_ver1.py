# Lab 12: Contact List
# Version 1
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



### This list comprehension method is the same as below:
# weather_list = []
# for value in values:
#     data = {}
#     for key, value in zip(keys, value):
#         data[key] = value
#     weather_list.append(data)


print(f"weather: {weather_list}")


