function checkCC (inputNum) {
    // convert to string then split to array
    inputNum = inputNum.toString().split('')
    // remove last digit and save for evaluation later
    let checkDigie = inputNum.pop()
    // declare variable for sum of numbers
    let numSum = 0
    // iterate through numbers in list
    inputNum.forEach(function (thisDigie, i) {
        // multiply every other number by 2
        if (i % 2 != 0) {
            thisDigie *= 2
            // subtract 9 if the result is over 9
            if (thisDigie > 9) {
                thisDigie -= 9
            }
        }
        // sum all digits after manipulation
        numSum += thisDigie
    })
    // compare last digit of numSum to checkDigie
    if (numSum % 10 == checkDigie) {
        return true
    } else {
        return false
    } 
}

// prompt for input
let inputNum = prompt('Gimme your credit card: ')

// display results from function
if (checkCC(inputNum)) {
    alert('Valid!')
} else {
    alert('Invalid.')
}