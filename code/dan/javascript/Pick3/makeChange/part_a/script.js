let amount = prompt("Please enter a dollar amount")



let quarters = amount / 25 
amount % 25
console.log(amount)
let dimes = amount / 10
amount %= 10
console.log(amount)
let nickels = amount / 5
amount += amount % 5
console.log(amount)
let pennies = amount  / 1
console.log(amount)
console.log (`'This uses' ${quarters} 'quarters', ${dimes} 'dimes' , ${nickels} 'nickels' , ${pennies} 'pennies'`) 