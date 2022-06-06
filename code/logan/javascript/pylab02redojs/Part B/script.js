let nums = []
let total = 0
let avg = 0

let input = document.querySelector('#input')
const button1 = document.querySelector('#button1') // for adding
// const button2 = document.querySelector('#button2') // for averaging
const totalOut = document.querySelector('#totalOut')
const avgOut = document.querySelector('#avgOut')

button1.addEventListener('click', function () {

    total += +input.value
    nums.push(+input.value)

    totalOut.innerText = total

    avg = (total/nums.length)

    avgOut.innerText = avg

})

// button1.addEventListener('click', function () {

//     avg = total

// })