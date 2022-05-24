// declare converter object
let converter = {
    in: .0254,
    ft: .3048,
    yd: .9144,
    mi: 1609.34,
    m: 1,
    km: 1000,
}

// prompt for length and units
let startDistance = prompt('Please enter a length/distance to convert: ')
let startUnit = prompt('Please enter the unit of measurement for that length/distance (valid options are in, ft, yd, mi, m, & km): ')
let endUnit = prompt('Please enter the unit of measurement you would like to convert to (valid options are in, ft, yd, mi, m, & km): ')

// perform conversion and assign to variable
let endDistance = startDistance * converter[startUnit] / converter[endUnit]

// display results
alert(`${startDistance} ${startUnit} is equal to ${endDistance} ${endUnit}`)