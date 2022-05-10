

let payouts_for_matches = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

let num_of_winning_tickets = 0
let balance = 0
let expences = 0

let number_list = [num for num in range(1, 100)]


function pick6():
    //"""return a list of 6 random numbers"""
    return random.sample(number_list, 6)


function num_matches(winning_ticket, ticket):
    //"""return the number of matches between the 2 tickets"""
    match_count = 0
    for inx, num in enumerate(winning_ticket):
        if ticket[inx] == num:
            match_count += 1
    return match_count

    
let winning_numbers = pick6()


for _ in range(100000):
    let ticket_numbers = pick6()
    let balance -= 2
    let expences -= 2

    let matches = (num_matches(winning_ticket=winning_numbers, ticket=ticket_numbers))
    
    if matches:
        num_of_winning_tickets += 1
    
    balance += payouts_for_matches[str(matches)]



return_on_investment = round(((balance - expences)/expences * 100), 2)

alert(`****** This gambling simulator just played the 'Pick Six' lottery 100,000 times. ******
      \n
      \nThere were ${num_of_winning_tickets} winning tickets.
      \nStarting at $0.00, the final balance after 100,000 games is:  ${balance:.2f}
      \n
      \nYour ROI (Return On Investment) is: ${return_on_investment}%`
)