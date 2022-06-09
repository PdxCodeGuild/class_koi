// declare converter object
let converter = {
    in: .0254,
    ft: .3048,
    yd: .9144,
    mi: 1609.34,
    m: 1,
    km: 1000,
}
// get elements
let startDistance = document.querySelector('#start-distance')
let startUnit = document.querySelector('#start-unit')
let endUnit = document.querySelector('#end-unit')
let results = document.querySelector('#results')


// assign button to variable and add event listener
let submitButton = document.querySelector('#submit-button')
submitButton.addEventListener('click', function() {
    // perform conversion and assign to variable
    let endDistance = startDistance.value * converter[startUnit.value] / converter[endUnit.value]

    // display results
    results.innerHTML = `${startDistance.value} ${startUnit.value} is equal to ${endDistance} ${endUnit.value}`
})