// Lab 01 Unit Converter
// Part B

const input = document.querySelector('#input')
const button1 = document.querySelector('#button1')


let convertFrom = document.querySelector('#convertFrom')
let convertTo = document.querySelector('#convertTo')

const conversions = {
    ft : 0.3048,
    mi : 1609.34,
    cm : 0.01,
    m : 1,
    km : 1000,
    yd : 0.9144,
    in : 0.0254
}

function convert(x, y, z){
    return (x*y)/(z)
}
console.log(conversions[convertFrom.value])

button1.addEventListener('click', function() {
    const distance = +input.value
    console.log(distance, typeof distance)
    const conversion_output = convert(distance, conversions[convertFrom.value], conversions[convertTo.value])
    output.innerText = `${distance} ${convertFrom.value} is ${conversion_output} ${convertTo.value}`
    console.log(convertFrom.value, typeof convertFrom.value)
    console.log(convertTo.selectedOptions[0].innerText)
})

