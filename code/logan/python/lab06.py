import random

balance = 0

def payout(x):
    if x == 0:
        return (0 - 2)
    elif x == 1:
        return (4 - 2)
    elif x == 2:
        return (7 - 2)
    elif x == 3:
        return (100 - 2)
    elif x == 4:
        return (50000 - 2)
    if x == 5:
        return (1000000 - 2)
    if x == 6: 
        return (25000000 - 2)



def pick6():
    ticket = []
    for i in range(0,6):
        selection = str(random.randint(1, 99))
        ticket.append(selection)
    return ticket

def num_matches(tick1, tick2):
    matchset = []
    for x in tick1:
        comp_val = tick1.index(x)
        if x == tick2[comp_val]:
            matchset.append(1)
    return len(matchset)

while True:
    try:
        how_many = int(input("\nHow many times would you like to play?...\n"))
        break
    except:
        print("Invalid input.  Please input a number as a digit.")

for cycles in range (0,how_many):
    your_ticket = pick6()
    dealer_ticket = pick6()
    balance += payout(num_matches(your_ticket, dealer_ticket))


print(f"\n{balance}\n")



# print(your_ticket)
# print(dealer_ticket)
# print(num_matches(your_ticket, dealer_ticket))


