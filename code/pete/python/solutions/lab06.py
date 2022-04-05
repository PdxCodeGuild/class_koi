from multiprocessing.sharedctypes import Value
import random

def pick6():
    """return a list of 6 random numbers from 1-99"""
    # random.sample takes in a sequence (like a list or string) and k (number of items)
    # and returns a new list with k unique items from the sequence
    # random.sample(sequence, k)
    return random.sample(range(1, 100), 6)

    ticket = []
    for _ in range(6): # _ indicates it is an unused variable
        while True: # this while loop is checking to make sure a number
            # isn't already in the list
            number = random.randint(1, 99)
            if number in ticket:
                continue # go back to the top of the loop, don't execute remaining loop code
            ticket.append(number)
            break
            
    return ticket


def num_matches(ticket1, ticket2):
    """given two lists of equal length, returns the number of
    indices where the element is the same for both lists"""
    if len(ticket1) != len(ticket2): # this is just a check to see that the lists have an equal length
        raise ValueError('Lists must be of equal length')
    matches = 0

    # # for i in range loop
    # for i in range(len(ticket1)):
    #     if ticket1[i] == ticket2[i]:
    #         matches += 1
    
    # # using enumerate
    # for i, number in enumerate(ticket1):
    #     if number == ticket2[i]:
    #         matches += 1

    for number1, number2 in zip(ticket1, ticket2):
        if number1 == number2:
            matches += 1
    
    return matches

matches_to_cashes = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000,
}


if __name__ == '__main__': # if this module is the "main" module, or the one which is directly run

    # Generate a list of 6 random numbers representing the winning ticket
    winning_ticket = pick6()
    # Start your balance at 0
    balance = 0
    earnings = 0
    expenses = 0
    # Loop 100,000 times, for each loop:
    for _ in range(1_000_000):
        # Generate a list of 6 random numbers representing the ticket
        ticket = pick6()
        # Subtract 2 from your balance (you bought a ticket)
        balance -= 2
        expenses += 2
        # Find how many numbers match
        matches = num_matches(winning_ticket, ticket)
        # Add to your balance the winnings from your matches
        balance += matches_to_cashes[matches]
        earnings += matches_to_cashes[matches]
    # After the loop, print the final balance
    print(balance)
    print((earnings - expenses) / expenses)
    # for _ in range(6):
    #     print(pick6())

    # print(num_matches([1, 2, 3, 4], [1, 2, 3]))

    # print(num_matches([1, 2, 3], [4, 5, 6]))
    # print(num_matches([4, 5, 6], [4, 5, 6]))
    # print(num_matches([1, 5, 6], [4, 5, 6]))

    # num_matches([1, 2, 3], [4, 5])