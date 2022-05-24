let dollarAmount = parseFloat(prompt("Please enter a dollar amount as a decimal number:  "))

let dollarAdj = parseInt((dollarAmount * 100))

let running_total = 0
let quarters = Math.floor((dollarAdj / 25 ))
running_total = (dollarAdj % 25)
let dimes = Math.floor((running_total / 10))
running_total = (running_total % 10)
let nickels = Math.floor((running_total / 5))
let pennies = (running_total % 5)

alert(`dollar amount: ${dollarAmount}`)
alert(`dollar amount * 100: ${dollarAdj}`)
alert(`That's ${quarters} quarters, ${dimes} dimes, ${nickels} nickels, and ${pennies} pennies.`)