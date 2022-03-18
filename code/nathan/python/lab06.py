import random
'''
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
'''

def pickSix():
# Generate a list of 6 random numbers representing the winning ticket
    newList = []
    for i in range(6):
        newNum = random.randint(1, 99)
        while(newList.__contains__(newNum)):
            newNum = random.randint(1, 99)
        newList.append(newNum)
    return newList

def numMatches(winningTicket, myTicket):
    count = 0
    for i in winningTicket:
        for j in myTicket:
            if(i == j):
                count += 1
    return count



def spendingMonies():

    prizes = {
        0 : 0,
        1 : 4,
        2 : 7,
        3 : 100,
        4 : 50000,
        5 : 1000000,
        6 : 25000000,
    }

    moneyLost = 0
    moneyWon = 0

    for i in range(100000):
        moneyLost += 2
        matches = numMatches(pickSix(), pickSix())
        moneyWon += prizes[matches]
    
    print(f"Money Spent = {moneyLost}\nMoney Won = {moneyWon}")
    print(f"ROI = {(moneyWon - moneyLost)/moneyLost}")

spendingMonies()






























