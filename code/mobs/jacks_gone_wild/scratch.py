"""
each iteration of aging function = 1 year
    iterate through each age group
        subtract the current population from that age
        add that population to the next age (in temp variable)

        if old enough to breed, add 2 per breeding pair to year 0

        if too old, kill em 
    

run function in while loop until population is >= 1000
    iterate number of years within loop

"""




def aging(input):
    # population placeholder
    temp_jack = input
    # iterate through each index position of input
    for x in range(len(input)):
        if x == 9:
            temp_jack[x] -= input[x]
        else:
            temp_jack[x + 1] = input[x]
            temp_jack[x] -= input[x]

    return temp_jack




# each index is an age group index 0= age 0 and each interger = population
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
    population = sum(jackalope)


    # 
    print(jackalope)








