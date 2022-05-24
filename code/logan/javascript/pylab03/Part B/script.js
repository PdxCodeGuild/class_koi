const button = document.querySelector('#button') // for getting the $ amt
const msgOut = document.querySelector('#msgOut') // show change total
let input = document.querySelector('#input')


// variable dec
let running_total = 0
let quarters = 0
let dimes = 0
let nickels = 0
let pennies = 0


button.addEventListener('click', function () {

dollarAdj = parseInt((+input.value * 100))

running_total = 0
quarters = Math.floor((dollarAdj / 25 ))
running_total = (dollarAdj % 25)
dimes = Math.floor((running_total / 10))
running_total = (running_total % 10)
nickels = Math.floor((running_total / 5))
pennies = (running_total % 5)

msgOut.innerText = `That's ${quarters} quarters, ${dimes} dimes, ${nickels} nickels, and ${pennies} pennies.`

})

// alert(`That's ${quarters} quarters, ${dimes} dimes, ${nickels} nickels, and ${pennies} pennies.`)