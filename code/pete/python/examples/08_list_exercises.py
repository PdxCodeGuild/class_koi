from random import shuffle
"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
seasons = ['spring', 'summer', 'fall', 'winter']
print(seasons[1])


"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]
# seasons2d = [
#     ['march', 'april', 'may'],
#     ['june', 'july', 'august'],
#     ['september', 'october', 'november'],
#     ['december', 'january', 'february'],
# ]
# summer == seasons2d[1] # they are the same thing
print(seasons2d[1][1])


"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""
seasons[2] = 'autumn'
print(seasons)


"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""
seasons2d[3][2] = 'february'
print(seasons2d)


"""
Loops
Loop over seasons to print out each season
"""
seasons = ['spring', 'summer', 'fall', 'winter']
for season in seasons:
    print(season)

"""
Loop over seasons to print out each season using range() and len()
"""
for x in range(len(seasons)): # x is an integer, the index of the season in the list
    print(x, seasons[x])
    seasons[x] = seasons[x].upper() # if you want to change something, you can use the index

# print(seasons)

"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""
seasons2d = [spring, summer, fall, winter]
for season in seasons2d:
    print(season)
    for month in season:
        print(month)


"""
Using range() and len(), loop over seasons2d to print out each month
"""
for i in range(len(seasons2d)):
    # print(seasons2d[i])
    for j in range(len(seasons2d[i])):
        print(seasons2d[i][j], f'seasons2d[{i}][{j}]')
        # for k in range(len(seasons2d[i][j])):
        #     print(seasons2d[i][j][k])
    # season = seasons2d[i]
    # for j in range(len(season)):
        # print(season[j])



"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries']

for item in items_to_add:
    print(item)
    if item not in grocery_list:
        grocery_list.append(item)

# if 'bananas' not in grocery_list:
#     grocery_list.append('bananas')
# if 'blueberries' not in grocery_list:
#     grocery_list.append('blueberries')
print(grocery_list)


"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.insert(0, 'mangos')
grocery_list.insert(10, 'cherries')
grocery_list.insert(-1, 'pop tarts')
print(grocery_list)
print(grocery_list.index('cherries'))

"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.remove('bananas')
print(grocery_list)

"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli from fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli']
vegetables = ['potatoes', 'radishes', 'celery']

# veg = fruits.pop(2)
# vegetables.append(veg)

vegetables.append(fruits.pop(2)) # one-liner
print(fruits, vegetables)


"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list)  # grocery_list is now randomly shuffled

# index = grocery_list.index('oranges')
# grocery_list.pop(index)

grocery_list.pop(grocery_list.index('oranges')) # one-liner
print(grocery_list)



"""
Remove all the mangos from too_many_mangos
"""

too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos',
                   'blueberries', 'mangos', 'oranges', 'mangos', 'mangos']

for i, fruit in enumerate(too_many_mangos):
    print(i, fruit)
    if fruit == 'mangos':
        too_many_mangos.pop(i)
    # if fruit == 'mangos':
    #     too_many_mangos.remove('fruit')

# while 'mangos' in too_many_mangos:
#     too_many_mangos.remove('mangos')

print(too_many_mangos)


"""
Slicing mylist[start:end:step]
Use slicing to print out a list of the programming langagues
"""

languages = ['Python', 'JavaScript', 'Japanese', 'English', 'Arabic', 'Greek', 'Hindi']
print(languages[:2])
# print(languages[:2:])

languages = ['Chinese', 'Spanish', 'Arabic', 'Python', 'JavaScript', 'C#', 'Java']
print(languages[3::])

languages = ['English', 'Thai', 'French', 'German', 'Rust', 'C', 'Go', 'Assembly', 'COBOL', 'Icelandic', 'Italian']
print(languages[4:9])


languages = ['JavaScript', 'English', 'French', 'Rust', 'Norwegian', 'Danish', 'Python']
print(languages[::3])


languages = ['Swahili', 'Go', 'Afrikaans', 'Java', 'Romansh', 'GDScript', 'Quechua']
print(languages[1::2])


"""
Use slicing to print out a list of the course sections in the order we will be covering them
"""
languages_frameworks_engines_etc = ['Unity', 'Angular', 'French', 'Django Rest Framework', 'Russian', 'Lua', 'Vue', 'Pascal', 'Godot', 'JavaScript', 'Korean', 'PHP', 'Django', 'Perl', 'Dutch', 'CSS', 'Express', 'HLSL', 'HTML', 'Unreal Engine', 'Dothraki', 'Flask', 'Elvish', 'Doggo-Speak', 'Python', 'High Valyrian', 'Morse Code', 'C++']
print(languages_frameworks_engines_etc[-4:2:-3])
