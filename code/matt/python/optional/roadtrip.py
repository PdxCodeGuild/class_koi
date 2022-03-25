'''
PDX Code Guild - Class Koi
Optional Lab - Road Trip
Matt Walsh
'''
 
# Version 1
""" 
# dictionary of cities and their direct destinations
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# function to add "&" before last item in list while joining
def join_list(list_to_join):
    return ', '.join(list_to_join[:-1]) + ', & ' + (list_to_join[-1])

def list_cities(starting):
    ending = [] # empty list for end destinations
    first_hop = [] # empty list to hold first hop cities
    # iterate through cities 1 hop from starting city and add to lists
    for destination in city_to_accessible_cities[starting]:
        ending.append(destination) 
        first_hop.append(destination)
    for city in first_hop: # iterate through first hop cities
        # iterate through destinations available from first hop cities
        for destination in city_to_accessible_cities[city]:
            # if destinations are not already on the list and are not the starting city, append them
            if destination not in ending and destination != starting:
                ending.append(destination)
    ending.sort() # sort the list
    return join_list(ending) # join into string while returning

while True:
    # ask for starting city
    starting = input('What city are you starting in? ').title()
    # if the starting city is in the list of cities, print results
    if starting in city_to_accessible_cities:
        print(f'\nDestinations available within 2 hops: {list_cities(starting)}')
        break
    # if the starting city is NOT in the list of cities, print a list of starting cities
    else:
        print(f'\nAvailable starting cities are: {join_list(list(city_to_accessible_cities))}\n')
 """


# Version 2

# dictionary of cities and their direct destinations
city_to_accessible_cities = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

# function to calculate shortest distance from starting location to all valid destinations
def list_cities(starting,hops):
    destinations = [] # empty list to store valid destinations
    destinations_with_time = {} # empty dictionary to add destinations to with shortest travel time
    # iterate through all valid destinations from starting point and add to list and dictionary
    for first_hop in city_to_accessible_cities[starting]:
        destinations_with_time[first_hop] = city_to_accessible_cities[starting][first_hop]
        destinations.append(first_hop)
    for x in range(hops - 1): # loop through the number of hops, minus the first since it's already accounted for
        # loop through each destination currently in destination list
        for dest in destinations: 
            for next_dest in city_to_accessible_cities[dest]: # loop through each next destination available
                # if the next destination is in the dictionary and travel time is shorter with the new route, update it in the dictionary
                if next_dest in destinations_with_time and destinations_with_time[dest] + city_to_accessible_cities[dest][next_dest] < destinations_with_time[next_dest]:
                    destinations_with_time[next_dest] = destinations_with_time[dest] + city_to_accessible_cities[dest][next_dest]
                # if the next destination is not in the list and is not the starting city, add it to the dictionary
                elif next_dest not in destinations_with_time and next_dest != starting:
                    destinations_with_time[next_dest] = destinations_with_time[dest] + city_to_accessible_cities[dest][next_dest]
        # loop through all destinations in destinations_with_time and add to destination list if not already there
        for dest_key in destinations_with_time:
            destinations.append(dest_key) if dest_key not in destinations else ''
    # return results
    return destinations_with_time

while True:
    # ask for starting city
    starting = input('What city are you starting in? ').title()
    # if the starting city is in the list of cities, print results
    if starting in city_to_accessible_cities:
        break
    # if the starting city is NOT in the list of cities, print a list of starting cities
    else:
        print(f'\nAvailable starting cities are: {join_list(list(city_to_accessible_cities))}\n')

while True:
    # ask for number of hops
    hops = input('How many times do you want to hop? ')
    # attempt to convert to integer
    try:
        hops = int(hops)
        break
    # if it can't be converted, display error and prompt for re-entry
    except:
        print('Please enter number of hops as a number.')

# Display results with each destination on a new line
print('\nYour available destinations are:')
for city in list_cities(starting,hops):
    print(f'{city}: {list_cities(starting,hops)[city]} hours')