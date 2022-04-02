'''
PDX Code Guild - Class Koi
Lab 07 - Jackalope Simulator
Matt Walsh

Version 1 done as mob with Team Jacks Gone Wild: Shaine, Matt, Dan, & Nathan
'''


# Version 1
''' 
def aging(input):
    """
    Ages and breeds jackalopes, takes in a list
    """
    # population placeholder
    temp_jack = [0,0,0,0,0,0,0,0,0,0]
    # iterate through each index position of input
    for x in range(len(input)):
        # If jacks are 'breeding age' add population to age 0 and age jacks
        if(x >= 3 and x <= 7):
            temp_jack[x + 1] = input[x]
            temp_jack[0] += input[x]
        # If jacks aren't of breeding age, age them
        elif(x != 9):
            temp_jack[x + 1] = input[x]
    # return updated population variable
    return temp_jack

# each index is an age group index 0= age 0 and each integer = population
jackalope  = [2,0,0,0,0,0,0,0,0,0]

# generate variables to track population and number of years
population = 0
years = 0

# run loop until population is at or above 1000
while population < 1000:
    # update jackalope variable with function output
    jackalope = aging(jackalope)
    # iterate year variable
    years += 1
    # update population variable with sum of jackalope list
    population = sum(jackalope)

print(f"It will take {years} years to get 1000 jackalope.")
'''


# Version 2

# import names to assign to jacks
from lab07_names import girl_names, boy_names
# import choice from random for sex and names and shuffle to reorder list
from random import choice, shuffle

# empty variable to hold jacks
jacks = []

def jack_gen(sex = None):
    """
    Generate new jacks
    """
    # empty dictionary to hold jack
    new_jack = {}
    # new jacks are 0 and not pregnant
    new_jack['age'] = 0
    new_jack['preg'] = False
    # randomly select sex unless specified in input
    if sex != None:
        new_jack['sex'] = sex
    else:
        new_jack['sex'] = choice(['m','f'])
    # set name based on sex
    if new_jack['sex'] == 'm':
        new_jack['name'] = choice(boy_names)
    else:
        new_jack['name'] = choice(girl_names)
    # return the populated dictionary
    return new_jack

def age_jacks(jacks):
    """
    Age or kill jacks
    """
    # iterate through jacks in reverse order
    for x in range(len(jacks)):
        # set variable to reverse order of iteration
        y = len(jacks) - x - 1
        # kill jack once it reaches 10 years old
        if jacks[y]['age'] == 10:
            jacks.pop(y)
        # increase age of all others
        else:
            jacks[y]['age'] += 1
    # return updated jacks
    return jacks

def ready_to_breed(x,jacks):
    """
    Check to see if jack is ready to breed
    """
    # assign attributes of jack to variables
    sex = jacks[x]['sex']
    preg = jacks[x]['preg']
    age = jacks[x]['age']
    # check if all criteria are met
    if sex == 'f' and preg == False and age >= 4 and age <= 8:
        return True
    else:
        return False

def adjacent_male(x,jacks):
    """
    Check to see if adjacent jacks are suitable for breeding
    """
    # assign adjacent jacks to variables
    left = jacks[x - 1]
    # don't assign right jack if at end of list
    if x != len(jacks) - 1:
        right = jacks[x + 1]
    # check adjacent jacks and return True if viable breeding partner
    if x == 0:
        if right['sex'] == 'm' and right['age'] >= 4 and right['age'] <= 8:
            return True
    elif x == len(jacks) - 1:
        if left['sex'] == 'm' and left['age'] >= 4 and left['age'] <= 8:
            return True
    else:
        if left['sex'] == 'm' and left['age'] >= 4 and left['age'] <= 8:
            return True
        elif right['sex'] == 'm' and right['age'] >= 4 and right['age'] <= 8:
            return True

def breed_jacks(jacks):
    """
    Breed jacks when appropriate
    """
    # iterate through list of jacks
    for x in range(len(jacks)):
        # check to see if jacks are ready to breed
        if ready_to_breed(x,jacks) == True:
            # check to see if adjacent jacks are viable breeding partners
            if adjacent_male(x,jacks) == True:
                # make jack pregnant if all criteria are met
                jacks[x]['preg'] = True
        # if they're already pregnant, birth the baby and reset pregnancy
        elif jacks[x]['preg'] == True:
            jacks.append(jack_gen())
            jacks[x]['preg'] = False
    # return updated jack list
    return jacks


def year_loop(jacks,year_goal = None, pop_goal = None):
    """
    Loop through years until conditions are met
    """
    # assign year, population, and max population counters
    year_count = 0
    pop_count = 0
    max_pop = 0
    # loop until either year or population goal is met
    while True:
        # age jacks with function
        age_jacks(jacks)
        # breed jacks with function
        breed_jacks(jacks)
        # increment year and update population
        year_count += 1
        pop_count = len(jacks)
        # increase max_pop if current population is larger
        if pop_count > max_pop:
            max_pop = pop_count
        # check to see if either goal is met and break if so
        if year_goal != None and year_count == year_goal:
            break
        elif pop_goal != None and pop_count >= pop_goal:
            break
        # break if population goal is set and population reaches 0
        elif pop_count == 0:
            break
    # shuffle jacks
    shuffle(jacks)
    # return the new jack dictionary with number of years and total population
    return jacks, year_count, pop_count, max_pop

# initialize our jack list with a male and female
while len(jacks) < 2:
    # randomly generate first jack
    if len(jacks) == 0:
        jacks.append(jack_gen())
    # generate second jack with opposite sex
    else:
        jacks.append(jack_gen('f' if jacks[0]['sex'] == 'm' else 'm'))

# ask user whether they want to run based on year number of population goal
while True:
    print('''
You can run the simulation in years mode or pop mode.
Years mode will run the number of years you select.
Pop mode will run until population has reached the goal you set.
    ''')
    goal_type = input('Enter "years" or "pop" to choose: ')
    if goal_type == 'years' or goal_type == 'pop':
        print(f'You have selected {goal_type} mode.')
        break
    # if entry is invalid prompt for re-entry
    else:
        print('Try again.')

while True:
    # if user selected years, validate entry and generate results
    if goal_type == 'years':
        years = input('How many years would you like to run? ')
        try:
            years = int(years)
            result = year_loop(jacks,years,None)
            break
        # prompt for re-entry if input is invalid
        except:
            print('Please enter a number.')
    # if user selected population, validate entry and generate results
    else:
        pop = input('What is your target population? ')
        try:
            pop = int(pop)
            result = year_loop(jacks,None,pop)
            break
        # prompt for re-entry if input is invalid
        except:
            print('Please enter a number.')

# check if population is 0 and display appropriate results
if result[2] == 0:
    print(f'''
I'm sorry, all the jackalopes died after {result[1]} years.
At one point the herd had {result[3]} jackalope, but they're all dead now.''')
else:
    print(f'''
After {result[1]} years, there are {result[2]} jackalope in the herd!''')
    if result[3] > result[2]:
        print(f'The herd had as many as {result[3]} jackalope once.')
    else:
        print('This is the largest the herd has been!')