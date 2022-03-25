##Version 1##
##Code##

city_to_accessible_cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': {'New York'}
}

initial = [input("\nSelect a starting city...").title()]


def hop(value):
    next = []
    for x in value:
        for y in city_to_accessible_cities[x]:
            if y not in next:
                next.append(y)
    return next
    
hop1 = hop(initial)
hop2 = hop(hop1)

print(f"\n Immediate destinations: {hop(initial)}.")
print(f"\n After two hops: {hop2}.")

print("\n")