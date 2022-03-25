#Version 1 & 2


# Dictionary "Number of matches", "Jackpot Amount"
winnings_dict= {1:"$4",
                2: "$7",
                3 : "$100",
                4: "$50,000",
                5 : "$1,000,000",
                6 : "25,000,000"}

import random

#empty lists to append
ticket = []
winning_ticket = []
balance = 0
balance = -2

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
matches = 0
def num_matches(ticket, winning_ticket):
   global matches # global used to return matches outside of function 
for x in range (len(ticket)):
        if ticket[x] == winning_ticket[x]:
            matches += 1
        print (matches)
         

# print winner logic
if matches == 0:
   print("Sorry try again next time")
elif matches == 1:
   print (f"You've won {winnings_dict[1]} + {balance}")
elif matches == 2:
    print (f"You've won {winnings_dict[2]} + {balance}")
elif matches == 3:
    print (f"You've won {winnings_dict[3]} + {balance}")
elif matches == 4:
    print (f"You've won {winnings_dict[4]} + {balance}")
elif matches == 5:
    print (f"You've won {winnings_dict[5]} + {balance}")
elif matches == 6:
    print (f"You've won the grand prize {winnings_dict[6]} + {balance}")
    
    

for i in range (100000):
    pick6(ticket)
    num_matches(winning_ticket, ticket) 


ROI = balance + winning_ticket[]
    