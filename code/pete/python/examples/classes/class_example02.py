from dog import Dog

pax = Dog('Pax', 'Greyhound', 'large')
flynn = Dog('Flynn', 'Greyhound', 'large')
charlie = Dog('Charlie', 'Greyhound', 'large')

for greyhound in [charlie, flynn, pax]:
    print(type(greyhound))
    greyhound.bark()