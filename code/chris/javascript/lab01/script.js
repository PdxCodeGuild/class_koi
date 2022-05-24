
/** Version 1 */
// what is the distance in feet? 12
// 12 ft is 3.6576 m

/** Version 2 */
// allow the user to also enter the units then conver the distance to meters.
// allow feet, miles meters, kilometers
// What is the distance? 100
// what are the units? mi
// 100 mi is 160934 m

/** Version 3 */
// add support for yards and inches.

/** Version 4 */
// ask the user for output units as well
// What is the distance? 100
// What are the input units? ft
// What are the output units? mi
// 100 ft is 0.0189394 mi

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - //
// Version 4 //
let unitsDict = {
    'feet': .3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': .9144,
    'inches': .0254,
}
function conversions(inputValue, inputUnits, outputUnits) {
    let meterValue = inputValue * unitsDict[`${inputUnits}`]
    let convertedValue = meterValue / unitsDict[`${outputUnits}`]
  return convertedValue;
}

let btConvert = document.querySelector('#btConvert')
console.log(btConvert)
btConvert.onclick = function() {
    let inputValue = document.querySelector('#input_value').value;
    let inputUnits = document.querySelector('#input_units').value;
    let outputUnits = document.querySelector('#output_units').value;
    outputValue = conversions(inputValue, inputUnits, outputUnits);
    document.getElementById('result').innerHTML = `${inputValue} ${inputUnits} is ${outputValue} ${outputUnits}.`

}