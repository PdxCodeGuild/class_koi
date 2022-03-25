
nums = []
for x in range(10):
    nums.append(x**2)



nums = [x**2 for x in range(10)]






numbers = [1, 2, 3, 4, 5]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)



evens = [number for number in numbers if number % 2 == 0]






"""
EXERCISE 1
Translate for loop to list comprehension
"""
hats = ['baseball cap', 'fedora', 'derby', 'panama']

for hat in hats:
	print(hat)

# list comprehension version...
hats = [print(hat) for hat in hats]
print(hats) # [None, None, None, None]


"""
EXERCISE 2
Translate for loop to list comprehension
"""
dogs = ['pluto', 'fido', 'clifford', 'lassie']
dog_facts = []
for dog in dogs:
	dog_facts.append(f"{dog.capitalize()} is a good boy.")
print(dog_facts)

# list comprehension version...
# dog_facts = [f"{dog.capitalize()} is a good boy." for dog in dogs]
dog_facts = [dog.capitalize() + ' is a good boy.' for dog in dogs]
print(dog_facts)


"""
EXERCISE 3
Translate for loop to list comprehension
"""
numbers = [1, 238, 74, 364, 65, 23, 765]
evens = []
odds = []
for number in numbers:
	if number % 2 == 0:
		evens.append(number)
	else:
		odds.append(number)
# list comprehension version
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 == 1]
print(evens, odds)


numbers = [1, 2.723, 238, 74, 0.234, 0.43890, 364, 65, 23, 765]

evens = []
odds = []
[evens.append(number) if number % 2 == 0 else odds.append(number) for number in numbers if type(number) is int]
print(evens, odds)

for number in numbers:
    if type(number) is int:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
"""
EXERCISE 4
Translate for loop to list comprehension
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
seasons2d = [spring, summer, fall, winter]

for season in seasons2d:
    print(season)
    for month in season:
        print(month)

# list comprehension version...

[[print(month) for month in season] and print(season) for season in seasons2d]

capitalized_months = [[month.capitalize() for month in season] for season in seasons2d]
print(capitalized_months)