

let conversion_ratios = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254,
}


let number_input = document.getElementById('number_input')
let unit_from = document.getElementById('input_unit')
let unit_to = document.getElementById('output_unit')
let convert_button = document.getElementById('convert_button')
let output_div = document.getElementById('output_div')



convert_button.onclick = function() {
    let number = number_input.value
    let meters_output = number * conversion_ratios[unit_from.value]
    let output = meters_output / conversion_ratios[unit_to.value]


    output_div.innerText = `${number} ${unit_from.value} \nis equal to\n${output.toPrecision(3)} ${unit_to.value}`
}




