miles_morales = {
    'superhero': 'Spider-Man',
    'age': 17,
    'home': 'New York City',
    'family': ['Jefferson Davis', 'Rio Morales'],
    'occupation': 'student',
    # 'secret identity': 'Miles Morales',
}

"""
Access: dict[key] or dict.get(key)
Access the 'superhero' key to print Miles' superhero name
"""
print(miles_morales['superhero'])
print(miles_morales.get('superhero'))

# dict[keyname] will raise a KeyError if the key is not in the dictionary
# print(miles_morales['secret identity']) # KeyError: 'secret identity'
print(miles_morales.get('secret identity'))

# dict.get(keyname) will return None if the key is not in the dictionary

secret_identity = miles_morales.get('secret identity')
if secret_identity is not None:
    print(f'The secret identity is {secret_identity}.')
else:
    print('No secret identity.')

"""
Update: dict[key] = value
Happy Birthday Miles 🎂
Increase Miles' age by 1
"""
# miles_morales['age'] = 18
miles_morales['age'] += 1
print(miles_morales)

def happ_birthday():
    miles_morales['age'] += 1

# happ_birthday()
# print(miles_morales)
# happ_birthday()
# print(miles_morales)

"""
Add Miles' uncle, Aaron Davis, to the family value
"""
# print(miles_morales['family'])
miles_morales['family'].append('Aaron Davis')
print(miles_morales['family'])

# family = miles_morales['family']
# family.append('Aaron Davis')
# print(miles_morales)

# super_hero = miles_morales['superhero']
# super_hero = 'Batman'
# print(miles_morales)

"""
Add key/value pair: dict[key] = value
Add more info to the miles_morales dictionary
"""
miles_morales['secret identity'] = 'Miles Morales'
miles_morales['abilities'] = ['web slinging', 'spidey-sense']
miles_morales['abilities'].append('camouflage')
print(miles_morales)



"""dict.keys()"""
print(miles_morales.keys())

"""dict.values()"""
print(miles_morales.values())


"""dict.items()"""
print(miles_morales.items())

for key, value in miles_morales.items():
    print(f'The {key} is {value}.')

for thing in miles_morales: # gives the keys
    print(thing)

for thing in miles_morales.items():
    # print(thing)
    print(thing[0], thing[1])