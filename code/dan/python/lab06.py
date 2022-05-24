#Version 1 & 2


# Dictionary "Number of matches", "Jackpot Amount"
winnings_dict= {
                0:0,
                1:4,
                2: 7,
                3 : 100,
                4: 50_000,
                5 : 1_000_000,
                6 : 25_000_000,
}
import random

#empty lists to append
ticket = []
winning_ticket = []
balance = 0
expense = 0

# takes in a list adds 6 random numbers to list
def pick6(list):
    """
    return a list of 6 random numbers
    """
    for x in range(6):
      x = random.randint(1,99)
      list.append(x)
    return list 
 
# print function passing in empty list variables  
print(pick6(ticket))
print(pick6(winning_ticket))

# function to check numbers in ticket & winning ticekt match in correct index

def num_matches(ticket, winning_ticket):
    matches = 0
    #global matches # global used to return matches outside of function 
    for x in range (len(ticket)):
            if ticket[x] == winning_ticket[x]:
                matches += 1
    return matches

print (num_matches(ticket, winning_ticket))
    
         

# print winner logic
#if matches == 0:
   #print("Sorry try again next time")
#elif matches == 1:
  # print (f"You've won {winnings_dict[1]} + {balance}")
#elif matches == 2:
   # print (f"You've won {winnings_dict[2]} + {balance}")
#elif matches == 3:
    #print (f"You've won {winnings_dict[3]} + {balance}")
#elif matches == 4:
    #print (f"You've won {winnings_dict[4]} + {balance}")
#elif matches == 5:
    #print (f"You've won {winnings_dict[5]} + {balance}")
#elif matches == 6:
    #print (f"You've won the grand prize {winnings_dict[6]} + {balance}")
    
earnings = 0

for i in range (100_000):
    empty_ticket= []
    empty_win = []
    winner = pick6(empty_win)
    
    ticket = pick6(empty_ticket)
    matches = num_matches(ticket, winner) 
    balance -= 2
    expense += 2
    balance += winnings_dict[matches]
    earnings += winnings_dict[matches]
    
    
print(matches)   
print (balance)
print ((earnings - expense)/expense)
    



    