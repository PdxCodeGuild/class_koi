import random    
    # What I NEED TO DO
    # Add up how many numbers match
    # make program assign a score to matches.

def pick6():
    """
    return a list of 6 random numbers
    """
    # from stackoverflow --------------------
    winnig_ticket = random.sample(range(100), 6)
    
    return winnig_ticket


def calculate_points(winning_ticket, players_ticket):
    points = 0

    if winning_ticket[0] == players_ticket[0]: 
        points += 1

    if winning_ticket[1] == players_ticket[1]: 
        points += 1

    if winning_ticket[2] == players_ticket[2]: 
        points += 1    

    if winning_ticket[3] == players_ticket[3]: 
        points += 1     

    if winning_ticket[4] == players_ticket[4]: 
        points += 1

    if winning_ticket[5] == players_ticket[5]: 
        points += 1
    
    return points
    
winning_ticket = pick6()

i = 0
prize = 0

for i in range(100000):
    
    players_ticket = random.sample(range(100), 6)
    
    points = calculate_points(winning_ticket, players_ticket)
    if points == 1:
        prize += 2
    if points == 2:
        prize += 7
    if points == 3:
        prize += 100
    if points == 4:
        prize += 50000
    if points == 5:
        prize += 1000000
    if points == 6:
        prize += 25000000
        print("Grand Prize Winner!")
        break            
    i+=1

cost = 2*i

print(f'You won ${prize - cost} with {i} tickets. Congratulations!')

#Version 2
print(f'Your return on invesment was ${(prize - cost) / cost} per dollar spent. \n Earnings: ${prize} \n Cost: ${cost}')
