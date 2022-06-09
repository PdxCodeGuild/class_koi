import csv

with open(r"C:\Users\Brandon\Desktop\PDXCode\class_koi\code\brandon\python\lab12\cities.csv") as csv_cities:
    # lines = csv_cities.readlines() # this gives you a list with 'string value\n` there is a newline at the end
    # this gives you the lines w/o \n character
    lines = csv_cities.read().split('\n')

# print(lines)
# lines is a list of each line in the csv file
# your goal is to turn it into a list of dictionaries:

# print(lines)

# --------------------------------- VERSION 1 --------------------------

headers = lines[0].split(', ')


for header in headers:
    header = header.split(',')

x = []
a = 0
i = 0
city_dict = {}
city_list = []

print(lines)


def convertList(list):
    str = ''

    for i in list:
        str += i

    return str


def citydict():

    for city in lines[1::]:
        city = city.split(',')

        # combines headers/value dict Found ONLINE
        cities_split = zip(header, city)
        cities_split2 = dict(cities_split)

        dictionairy_copy = cities_split2.copy()  # copies all dicts to a list
        x.append(dictionairy_copy)
    return x


# --------------------------------- VERSION 2 --------------------------
user_input = input(
    'Would you like to [c]reate, [r]etrieve, [u]pdate, or [d]elete a record? ')


def cities(x):
    '''
    Creates a list of city names that should take updated input.
    '''
    a = 0
    while a < len(x):
        city_list.append(x[a]['name'])
        a += 1


def create_record():

    if user_input == 'c':
        play_again = 'Y'
        create_list = []

        while play_again == 'Y':
            cityname = input(
                f'What city would you like to create in addition to the following? {city_list}. ').title()
            create_list.append(cityname)
            city_list.append(cityname)

            country = input(
                f'What is the name if the country {cityname} is located in? ').title()
            create_list.append(country)

            population = input(
                f'What is the population of {cityname}? ').title()
            create_list.append(population)

            food = input(
                f'What type of food does {cityname} like to eat? ').title()
            create_list.append(food)

            mayor = input(f'Who is the mayor of {cityname}? ').title()
            create_list.append(mayor)

            climate = input(
                f'What kind of climate does {cityname} have? ').title()
            create_list.append(climate)

            combiner = zip(header, create_list)
            create_combined = dict(combiner)

            print(f'New information input for {cityname}')
            x.append(create_combined)
            play_again = input(
                f'Would you like to create another city? {city_list} Y or N ').title()


def retrieve_record():
    if user_input == 'r':
        play_again = 'Y'

        while play_again == 'Y':
            value = input(
                f'What city would you like to examine further? {city_list}. ').title()
            # i = 0

            # while i < len(x):
            #     i += 1               # takes user input and finds key/value and prints the dict out

            if value in x[i]['name']:
                print(x[i])
                # i += 1
            if value:
                play_again = input(
                    'Would you like to search for another city? Y or N ').title()
                continue

            else:
                play_again = input(
                    'No city was found. Would you like to search for another city? Y or N ').title()
                continue


def update_record():

    if user_input == 'u':
        play_again = 'Y'

        while play_again == 'Y':
            updated_record = input(
                f'Which city would you like to update? {city_list} ').title()

            for i in range(len(x)):
                if updated_record in x[i]['name']:

                    atribute = input(
                        f'Which atribute for {updated_record} would you like to change? Please choose from {header} ')

                    if atribute in header:
                        update_atribute = input(
                            f'What would you like to update {atribute} to? ')
                        x[i][atribute] = update_atribute
                        if atribute == 'name':
                            del city_list[i]
                            city_list.append(update_atribute)
                        print(x[i])
                        play_again = input(
                            f'Would you like to update anymore? Y or N ').title()

                else:
                    print(
                        f'Please enter a proper atribute name. STARTING OVER! {header} ')


def delete_record():

    if user_input == 'd':
        play_again = 'Y'

        while play_again == 'Y':
            deleted = input(
                f'Which entry would you like to delete in {city_list}? ').title()

            for i in range(len(x)):

                if x[i]['name'] == deleted:
                    del x[i]
                    del city_list[i]
                    break
            play_again = input(
                f'{deleted} deleted. Would you like to delete anymore cities? {city_list} Y or N ').title()


citydict()
cities(x)

create_record()
retrieve_record()
update_record()
delete_record()

# # #--------------------------------- VERSION 3 --------------------------

csv_list = [header]
a = ''

for i in x:
    t = list(i.values())
    a = convertList(t)

    csv_list.append(t)
print(csv_list)


with open(r"C:\Users\Brandon\Desktop\PDXCode\class_koi\code\brandon\python\lab12\cities.csv", 'w',) as f:
    for line in csv_list:
        for cell in line:
            f.write(cell + ',')
        line.pop(-1)
        f.write("\n")
