'''
SHAINE
MATT
DAN
NATHAN

TEAM JACKS GONE WILD!!
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
    print(f"{jackalope} {population}")

print(f"It will take {years} to get 1000 jackalope.")