
let nums = []
let running_sum = 0


let number_input = document.getElementById('number_input')
let submit_input_button = document.getElementById('submit_input_button')
let output_div = document.getElementById('output_div')


    
submit_input_button.onclick = function() {
    let number = number_input.value
    nums.push(parseInt(number))
    running_sum += parseInt(number)
    let average = running_sum / nums.length;
    output_div.innerText = `The average of "${nums}" is: ${average.toPrecision(3)}`
}







