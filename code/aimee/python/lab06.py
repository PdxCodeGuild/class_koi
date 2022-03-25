# Lab 06, Pick6 ---- #
from random import randint

prizes = {
    'ticket':2,
    '1':4,
    '2':7,
    '3':100,
    '4':50000,
    '5':1000000,
    '6':25000000,
}

def pick6():
    '''
    return a list of 6 random numbers
    '''
    ticket = []
    for i in range(6):
       ticket.append(randint(1, 99))
    return ticket

# using function to save values to winning ticket
winning_ticket = pick6()
print(winning_ticket)
user_ticket = pick6()
print(user_ticket)
       

def num_matches(winning_ticket, user_ticket):
    """
    return the number of matches between the 2 tickets
    """
    matches = 0 # starting matches is zero
    for i in range(6): # if any ints from either list of 6 match
        if winning_ticket[i] == user_ticket[i]:
            matches += 1 # add 1 to match for each match?
        return matches

ticket_matches = num_matches(winning_ticket, user_ticket)
print(ticket_matches)

'''
[10, 69, 12, 20, 10, 5]
[81, 86, 44, 20, 21, 60]
0 - isn't working, had 1 match
'''


    




# winning_ticket = []
# for i in range(0, 6):
#     x = random.randint(1, 99)
#     winning_ticket.append(x)
#     print(f'The winning ticket is {winning_ticket}')
    