// assign elements to variables
let submitButton = document.querySelector('#submit-button')
let results = document.querySelector('#results')
let numTicketsField = document.querySelector('#num-tickets')

// assign prize values to variable
let prizeValue = [0,4,7,100,50000,1000000,25000000]

// assign starting values to variables
let balance = 0
let spent = 0
let winningTickets = 0

// ticket generation function
function pick6 () {
    // make empty ticket
    let ticket = []
    for (let i = 0; i < 6; i++) {
        ticket.push(Math.floor(Math.random() * 100))
    }
    return ticket
}

// save winning ticket
let winningTicket = pick6()

// find number of matches
function numMatches (winningTicket, playerTicket) {
    // declare variable to hold number of matching digits
    let matchingDigies = 0
    // find matching digits
    for (let i = 0; i < 6; i++) {
        if (winningTicket[i] == playerTicket[i]) {
            matchingDigies++
        }
    }
    return matchingDigies
}

// adjust balance based on number of matches
function adjustBalance (numMatches) {
    let balanceChange = prizeValue[numMatches]
    return balanceChange
}

// display money properly
function processMoney (money) {
    return Math.abs(money).toLocaleString("en-US", {style:"currency", currency:"USD"})
}

// check tickets and adjust balance based on matches
function checkTickets (numTickets) {
    for (i = 0; i < numTickets; i++) {
        let matches = numMatches(winningTicket,pick6())
        if (matches > 0) {
            winningTickets++
        }
        balance += adjustBalance(matches)
        spent += 2
    }
}

// change winningTickets number variable into string with ticket/tickets
function winningTicketsString (winningTickets) {
    let winningTicketsString = winningTickets.toString()
    if (winningTickets == 1) {
        winningTicketsString += ' ticket'
    } else {
        winningTicketsString += ' tickets'
    }
    return winningTicketsString
}

// wrap lines in <p> tags
function wrapInP (linesVar) {
    wrappedInP = ''
    linesVar.forEach(function (line) {
        wrappedInP += `<p>${line}</p>`
    })
    return wrappedInP
}

// figure out if in total money was won or lost
function wonLost(balance, spent) {
    if (balance - spent > 0) {
        return 'won'
    } else {
        return 'lost'
    }
}

// calculate and display results
submitButton.addEventListener('click', function() {
    // reset values
    balance = 0
    spent = 0
    winningTickets = 0
    // get value of numTicketsField
    let numTickets = numTicketsField.value
    checkTickets(numTickets)
    // make empty array to hold results
    let linesVar = []
    // add lines
    linesVar.push(`After playing ${numTickets} times:`)
    linesVar.push(`- you spent ${processMoney(spent)}`)
    linesVar.push(`- you won ${processMoney(balance)}`)
    linesVar.push(`- ${winningTicketsString(winningTickets)} had at least one match`)
    linesVar.push(`In total, you ${wonLost(balance, spent)} ${processMoney(balance - spent)}.`)
    linesVar.push(`Your ROI for this session is ${((balance - spent)/spent).toFixed(2)}`)
    // display results
    results.innerHTML = wrapInP(linesVar)
})