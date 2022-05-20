const button = document.querySelector('#button') // click to submit
const msgOut = document.querySelector('#msgOut')
let input = document.querySelector('#input')

let standard_s = "abcdefghijklmnopqrstuvwxyz"
let rot13_s = "nopqrstuvwxyzabcdefghijklm"
let message = ""
// let newLetInd

function swapRot13(string) {
    let encodedString = ""
    // let stringLower = string.toLowercase()
    // gonna try without case support first



    for (let i=0; i<string.length; ++i) {
        // if (string[i] in standard_s == true) {
        if (standard_s.includes(string[i]) == true) {
            let newLetInd = standard_s.indexOf(string[i])
            encodedString = encodedString.concat(rot13_s[newLetInd])
    
        }
        else {
            encodedString = encodedString.concat(string[i])
        }
    
    }

    return encodedString
}

button.addEventListener('click', function () {
    message = input.value
    message = swapRot13(message)

    msgOut.innerText = message
    
    })