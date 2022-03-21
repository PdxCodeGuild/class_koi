import random

#Version 1



# play game 100,000 times



# 



def pick6():
    """
    return a list of 6 random numbers
    """
    # from stackoverflow --------------------
    winnig_ticket = random.sample(range(100), 6)
    winnings = 0
    
    for i in range(100000):
        
        # stack overflow
        players_ticket = random.sample(range(100), 6)
        #----------------------
        
        i+=1
        if players_ticket[0] == winnig_ticket[0] and players_ticket[1] == winnig_ticket[1] and players_ticket[2] == winnig_ticket[2] and        players_ticket[3] == winnig_ticket[3] and players_ticket[4] == winnig_ticket[4] and players_ticket[5] == winnig_ticket[5]:
            print(f"Grand Prize!!!")
            print(winnig_ticket, players_ticket)
            print(i)
            winnig_ticket = i
            winnings += 25000000
            return

        elif players_ticket[0] == winnig_ticket[0] and players_ticket[1] == winnig_ticket[1] and players_ticket[2] == winnig_ticket[2] and players_ticket[3] == winnig_ticket[3] and players_ticket[4] == winnig_ticket[4] or players_ticket[5] == winnig_ticket[5]:
            print('You found 5 numbers!')
            winnings += 1000000
            continue

        elif players_ticket[0] == winnig_ticket[0] and players_ticket[1] == winnig_ticket[1] and players_ticket[2] == winnig_ticket[2] and players_ticket[3] == winnig_ticket[3] or players_ticket[4] == winnig_ticket[4] or players_ticket[5] == winnig_ticket[5]:
            print('You found 4 numbers!')
            winnings += 50000
            continue

        elif players_ticket[0] == winnig_ticket[0] and players_ticket[1] == winnig_ticket[1] and players_ticket[2] == winnig_ticket[2] or players_ticket[3] == winnig_ticket[3] or players_ticket[4] == winnig_ticket[4] or players_ticket[5] == winnig_ticket[5]:
            print('You found 3 numbers!')
            winnings += 100
            continue

        elif players_ticket[0] == winnig_ticket[0] and players_ticket[1] == winnig_ticket[1] or players_ticket[2] == winnig_ticket[2] or players_ticket[3] == winnig_ticket[3] or players_ticket[4] == winnig_ticket[4] or players_ticket[5] == winnig_ticket[5]:
            print('You found 2 numbers!')
            winnings += 7
            continue

        elif players_ticket[0] == winnig_ticket[0]  or players_ticket[1] == winnig_ticket[1] or players_ticket[2] == winnig_ticket[2] or players_ticket[3] == winnig_ticket[3] or players_ticket[4] == winnig_ticket[4] or players_ticket[5] == winnig_ticket[5]:
            print('You found 1 number!')
            winnings += 2
            continue

    cost = 2*i

    print(f'Winnings: ${winnings}. Total cost: ${cost} You left the casion with: ${(winnings) - (cost)}')

    winnig_ticket = i
       
    def num_matches(winning_ticket, ticket):
        """
        return the number of matches between the 2 tickets
        """
        winning_ticket = winnig_ticket - ticket + 1
        if winnig_ticket == 100000:
            print('No winning ticket found. Try again. ')
        elif winning_ticket < 100000:
            print("Congrats!!!!!!!")
            print(winnig_ticket)
        
    num_matches(i, 1)

pick6()