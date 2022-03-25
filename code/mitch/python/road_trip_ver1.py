# Road Trip
# Version 1
# Mitch Chapman

city_to_accessible_cities = {
    'Boston': {'New York', 'Albany', 'Portland'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany'},
    'Philadelphia': {'New York'},
}

print("\nWelcome to the road trip helper. This will show you all of the cities connected to your starting city.")

#accepts a valid starting city for the hop outputs
while True:
    starting_city = input(f"Please enter your starting city. (Options are: {', '.join(list(city_to_accessible_cities.keys()))}) ").title()
    if starting_city in city_to_accessible_cities:
        break
    else:
        print("Error: Please enter a valid starting city.")


#references the dictionary to return the one hop cities
one_hop_cities = list(city_to_accessible_cities.get(starting_city))
print(f"\nThe following cities are connected to {starting_city} in one hop:\n{', '.join(one_hop_cities)}")


#references the dictionary for the two hop cities, excludes showing one hop cities, repeat two hop cities, and the starting city
two_hop_cities = []
for city in one_hop_cities:
    next = list(city_to_accessible_cities.get(city))
    for city in next:
        if city not in one_hop_cities and city not in two_hop_cities and city != starting_city:
            two_hop_cities.append(city)
      

print(f"\nThe following cities are connected to {starting_city} in two hops:\n{', '.join(two_hop_cities)}")


