let standard_s = "abcdefghijklmnopqrstuvwxyz"
let rot13_s = "nopqrstuvwxyzabcdefghijklm"

function swap_rot13(string) {
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

let message = ""
message = prompt("please input a message to be encrypted or decrypted with ROT13 in lowercase:  ")

message = swap_rot13(message)
alert(message)
// alert("huh")