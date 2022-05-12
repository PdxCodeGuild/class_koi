// javaScript Lab01 - Unit Converter

const distance = +prompt('Please enter the distance:')
console.log(distance, typeof distance)

const conversions = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000,
    yd : 0.9144,
    in : 0.0254
}

const units = prompt('What are the input units - in, ft, yd, mi, m, km: ')
console.log(units, typeof units)

//let conversion_units = conversions[units]
//console.log(conversion_units, typeof conversion_units)

const output_units = prompt('What are the desired output units - in, ft, yd, mi, m, km')

//let output = (distance*conversions[units])/(conversions[output_units])
//console.log(output, typeof output)


function convert(x, y, z){
    return (x*y)/(z)
}

//alert(distance + ' ' + units + ' is ' + output + ' ' + output_units)
const conversion_output = convert(distance, conversions[units], conversions[output_units])

alert(distance + ' ' + units + ' is ' + conversion_output + ' ' + output_units)