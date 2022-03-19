##Version2##
##Code##

# Dictionaries

import dis
from math import nextafter


city_to_accessible_cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': ['New York']
}

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

# Inputs
while True:
    initial = input("\nEnter a starting city...").title()
    if initial not in city_to_accessible_cities.keys():
        print("That's not a valid destination.")
    else:
        break
while True:
    try:
        num_hops = int(input("\nEnter a number of hops..."))
        break
    except:
        print("Invalid input.  Please input a number in digits.")

# Changing data types around

initial_ld = []
initiald = {}
initiald.update({initial: 0})
initial_ld.append(initiald)
feedvalue = initial_ld

# Generates 1 batch of permutations, stores all possible branch destinations paired with their travel times

def permutate(x):
    bigset = []
    for dict in x:
        listkeys = list(dict.keys())
        key = listkeys[0]
        subset = (city_to_accessible_cities_with_travel_time[key])
        for destination in list(subset):
            newentry = {}
            dist = dict[key] + subset[destination]
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

# Determines shortest possible trip to each city after a specified number of hops

# Boston

if len(distances_portland) > 0:
    next_boston = "3 hrs (1 hop)"
elif len(distances_new_york) > 0:
    next_boston = "4 hrs (1 hop)"
elif len(distances_albany) > 0:
    next_boston = "6 hrs (1 hop)"
elif len(distances_boston) > 0:
    next_boston = "6 hrs (2 hops)"
else:
    next_boston = "16 hrs (3 hops)"

# New York

if len(distances_boston) > 0:
    next_new_york = "4 hrs (1 hop)"
elif len(distances_albany) > 0:
    next_new_york = "5 hrs (1 hop)"
elif len(distances_portland) > 0:
    next_new_york = "7 hrs (2 hops)"
elif len(distances_new_york) > 0:
    next_new_york = "8 hrs (2 hops)"
else:
    next_new_york = "9 hrs (1 hop)"

# Albany

if len(distances_new_york) > 0:
    next_albany = "5 hrs (1 hop)"
elif len(distances_boston) > 0:
    next_albany = "6 hrs (1 hop)"
elif len(distances_portland) > 0:
    next_albany = "7 hrs (1 hop)"
elif len(distances_albany) > 0:
    next_albany = "10 hrs (2 hops)"
else:
    next_albany = "14 hrs (2 hops)"

# Portland

if len(distances_boston) > 0:
    next_portland = "3 hrs (1 hop)"
elif len(distances_portland) > 0:
    next_portland = "6 hrs (2 hops)"
elif len(distances_new_york) > 0 or len(distances_albany) > 0:
    next_portland = "7 hrs (2 hops)"
else:
    next_portland = "16 hrs (3 hops)"

# Philly

if len(distances_new_york) > 0:
    next_philly = "9 hrs (1 hop)"
elif len(distances_boston) > 0:
    next_philly = "13 hrs (2 hops)"
elif len(distances_albany) > 0:
    next_philly = "14 hrs (2 hops)"
elif len(distances_portland) > 0:
    next_philly = "16 hrs (3 hops)"
else:
    next_philly = "18 hrs (2 hops)"

# Output

print(f"""
Shortest {num_hops}-hop trips to each city:
Boston...{shortest_boston} hrs
New York...{shortest_new_york} hrs
Albany...{shortest_albany} hrs
Portland...{shortest_portland} hrs
Philadelphia...{shortest_philly} hrs

Shortest trip to each city after {num_hops} hops:
Boston...{next_boston}
New York...{next_new_york}
Albany...{next_albany}
Portland...{next_portland}
Philadelphia...{next_philly}
""")
