with open('code/pete/python/examples/data/cities.csv') as csv_cities:
    # lines = csv_cities.readlines() # this gives you a list with 'string value\n` there is a newline at the end
    lines = csv_cities.read().split('\n') # this gives you the lines w/o \n character
print(lines)

# lines is a list of each line in the csv file
# your goal is to turn it into a list of dictionaries:
cities = [
    {'name': 'Portland', 'country': 'USA', 'population': 652503, 'food': 'fusion', 'mayor': 'Ted Wheeler', 'climate': 'temperate'},
    {'name': 'Kansas City', 'country': 'USA', 'population': 508090, 'food': 'bbq', 'mayor': 'Quinton Lucas', 'climate': 'temperate'},
    # the rest of the cities...
]

# what you might want to do first is isolate the headers, or keys, from the rest of the lines
headers = lines[0]
print(headers, type(headers)) # name,country,population,food,mayor,climate <class 'str'>
headers = headers.split(',')
print(headers, type(headers))

# this is hard-coded, assuming you have a set number of cities
# city1 = lines[1].split(',')
# city2 = lines[2].split(',')
# city3 = lines[3].split(',')

# this code doesn't care about how many cities there are, it will loop over lines[1:], whether that's 1 or 1 million cities
for line in lines[1:]: 
    city = line.split(',')
    print(city)

for i in range(1, len(lines)):
    print(lines[i])

# print(city1, city2)