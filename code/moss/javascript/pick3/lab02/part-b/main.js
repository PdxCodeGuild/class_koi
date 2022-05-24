let numberInput = document.getElementById("number-input")
let numberArray = document.getElementById("number-array")
let avrgButton = document.getElementById("average-btn")
let avrgResult= document.getElementById("result")

let number_array = []

avrgButton.addEventListener("click", function() {

    let sum_number = 0

    let number = numberInput.value 
    console.log(`${number} is the input number`)

    number_array.push(number)
    console.log(`${number_array} is an array of input numbers`)

    for (let numberarrays of numberArray){
        sum_number += parseInt(numberarrays)
        console.log(sum_number)
    }
 
    let total = number_array.length
    console.log(total)

    let average = sum_number/total
    console.log(`${average} is the average`)

    numberArray.innerText = `Numbers : ${number_array}`
    avrgResult.innerText = `Average : ${average}`

})
