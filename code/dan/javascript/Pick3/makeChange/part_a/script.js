let amount = prompt("Please enter a dollar amount")


amount = parseFloat(amount) * 100
console.log(amount)


let quarters = (amount) / 25 
console.log(parseInt(quarters))
amount = parseFloat(amount) % 25
console.log(amount)

let dimes = amount / 10
if (parseFloat(amount) > 10){
    amount= parseFloat(amount) % 10
}
console.log(amount)

let nickels = amount / 5
amount = parseFloat(amount) % 5
console.log(amount)
let pennies = amount  / 1
amount = parseFloat(amount) % 1
console.log(amount)

console.log (`'This uses +' ${parseInt(quarters)} 'quarters', ${parseInt(dimes)} 'dimes' , ${parseInt(nickels)} 'nickels' , ${pennies} 'pennies'`) 