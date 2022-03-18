##Version2##
##Code##

# Dictionaries

city_to_accessible_cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': {'New York'}
}

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

# Inputs

initial = input("\nEnter a starting city...").title()
num_hops = int(input("\nEnter a number of hops..."))

# Changing data types around

initial_ld = []
initiald = {}
initiald.update({initial: 0})
initial_ld.append(initiald)
feedvalue = initial_ld

# Generates 1 permutation, stores all possible branch destinations paired with their travel times

def permutate(x):
    bigset = []
    for dict in x:
        listkeys = list(dict.keys())
        key = listkeys[0]
        subsubdict = (city_to_accessible_cities_with_travel_time[key])
        for destination in list(subsubdict):
            newentry = {}
            dist = dict[key] + subsubdict[destination]
            newentry.update({destination: dist})
            bigset.append(newentry)
    return bigset

# Repeats permutation as many times as user wants...I chickened out when I typed in '37' and bailed on my terminal.

for i in range (0, num_hops):
    permutate(feedvalue)
    feedvalue = permutate(feedvalue)

# Gather distances and determines shortest route

distances_boston = []
distances_new_york = []
distances_albany = []
distances_portland = []
distances_philly = []

for dict in feedvalue:
    listkeys = list(dict.keys())
    key = listkeys[0]
    if key == "Boston":
        distances_boston.append(dict["Boston"])
    elif key == "New York":
        distances_new_york.append(dict["New York"])
    elif key == "Albany":
        distances_albany.append(dict["Albany"])
    elif key == "Portland":
        distances_portland.append(dict["Portland"])
    elif key == "Philadelphia":
        distances_philly.append(dict["Philadelphia"])

if distances_boston == []:
    shortest_boston = "NA"
else:
    shortest_boston = min(distances_boston)

if distances_new_york == []:
    shortest_new_york = "NA"
else:
    shortest_new_york = min(distances_new_york)

if distances_albany == []:
    shortest_albany = "NA"
else:
    shortest_albany = min(distances_albany)

if distances_portland == []:
    shortest_portland = "NA"
else:
    shortest_portland = min(distances_portland)

if distances_philly == []:
    shortest_philly = "NA"
else:
    shortest_philly = min(distances_philly)

# Output

print(f"""
Shortest {num_hops}-hop flights to each city:
Boston...{shortest_boston} hrs
New York...{shortest_new_york} hrs
Albany...{shortest_albany} hrs
Portland...{shortest_portland} hrs
Philadelphia...{shortest_philly} hrs
""")