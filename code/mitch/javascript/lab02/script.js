

let conversion_ratios = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254,
}

function conversion_to_m(value, unit_from, unit_to){
    // """Converts input float to a float of another unit. Accepts inputs/outputs: 'ft', 'mi', 'm', 'km', 'yd', or 'in'."""
    let meters_output = value * conversion_ratios[unit_from]
    let unit_output = meters_output / conversion_ratios[unit_to]
    return unit_output.toPrecision(4)
}

let value = prompt("What is the distance? ")
let unit_from = prompt("What are the input units? ('ft', 'mi', 'm', 'km', 'yd', 'in') ")
let unit_to = prompt("What are the output units? ('ft', 'mi', 'm', 'km', 'yd', 'in') ")

let output = conversion_to_m(value, unit_from, unit_to)


alert(`${value} ${unit_from} is ${output} ${unit_to}`)