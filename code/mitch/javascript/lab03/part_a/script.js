

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
let earnings = 0
let expences = 0


// Return a list of 6 random numbers called number_list
function pick6(){
    let number_list = []
    for (let i = 0; i < 6; i++){
        number_list.push(Math.floor(Math.random() * 101))
    }
    return number_list
}


//"""re turn the number of matches between the 2 tickets"""
function num_matches(winning_ticket, ticket){
    let match_count = 0
    for (let i = 0; i < 6; i++){
        if (winning_ticket[i] == ticket[i]) {
            match_count += 1
        }
    }
    return match_count
}

let winning_numbers = pick6()


for (let i = 0; i < 100000; i++){
    let ticket_numbers = pick6()
    balance -= 2
    expences += 2

    let matches = num_matches(winning_numbers, ticket_numbers)

    if (matches){
        num_of_winning_tickets += 1
    }
    balance += payouts_for_matches[matches]
    earnings += payouts_for_matches[matches]
}


let return_on_investment = ( earnings - expences ) / expences * 100

alert(`****** This gambling simulator just played the 'Pick Six' lottery 100,000 times. ******
      \nThere were ${num_of_winning_tickets} winning tickets.
      \nStarting at $0.00, the final balance after 100,000 games is:  $${balance.toFixed(2)}
      \nYour ROI (Return On Investment) is: ${return_on_investment.toFixed(2)}%`
)