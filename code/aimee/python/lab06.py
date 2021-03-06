from random import randint

# version 1 ---------------------------------------- #

balance = 0
total_matches = 0
earnings = 0

def pick6():
    '''
    return a list of 6 random numbers
    '''
    ticket = []
    for i in range(6):
       ticket.append(randint(1, 99))
    return ticket

def num_matches(winning_ticket, user_ticket):
    """
    return the number of matches between the 2 tickets
    """
    match = 0
    if winning_ticket[0] == user_ticket[0]:
        match += 1
    elif winning_ticket[1] == user_ticket[1]:
        match += 1
    elif winning_ticket[2] == user_ticket[2]:
        match += 1
    elif winning_ticket[3] == user_ticket[3]:
        match += 1
    elif winning_ticket[4] == user_ticket[4]:
        match += 1
    elif winning_ticket[5] == user_ticket[5]:
        match += 1
    return match 

for x in range(1, 100001):
    winning_ticket = pick6()
    user_ticket = pick6()

    matches = num_matches(winning_ticket, user_ticket)
    
    if matches == 1:
        balance += 2 # accounting for cost of ticket
        total_matches += 1
    elif matches == 2:
        balance += 5
        total_matches += 2
    elif matches == 3:
        balance += 98
        total_matches += 3
    elif matches == 4:
        balance += 49998
        total_matches += 4
    elif matches == 5:
        balance += 999998
        total_matches += 5
    elif matches == 6:
        balance += 249999998
        total_matches += 6
    elif matches == 0:
        balance -= 2 # subtracts 2 if no matches
        
    if matches == 1:
        earnings += 4
    elif matches == 2:
        earnings += 7
    elif matches == 3:
        earnings += 100
    elif matches == 4:
        earnings += 50000
    elif matches == 5:
        earnings += 100000
    elif matches == 6:
        earnings += 25000000
        
print(f"You had {str(total_matches)} match(s). Your balance is ${str(balance)}.")  

# version 2 ---------------------------------------- #

# calculate ROI

expenses = 100000 * 2 # bought 100,000 tickets for $2 each

roi = float((earnings - expenses)/expenses)
print(f'You made ${earnings} in earnings, and spent ${expenses} for a return on investment of {roi}.')

