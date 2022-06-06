// #  *'-.-'*'-.-'*'-.-'*'--'*
// #     Project: Python 
// #   Lab 3: Make Change 
// #       Version: 1.0
// #   Author: Shaine Warren
// #   Email: mwarren86@gmail.com
// #       Date: Mar, 2022
// # *'-.-'*'-.-'*'-.-'*'--'*

document.getElementById("theButton").onclick = function(){
    let userInput = document.getElementById("textBox").value

    let userNum = userInput;

    const lowNum  = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
    }

    const highNum = {
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty', 
        6:'sixty', 
        7:'seventy', 
        8:'eighty',
        9:'ninety'
    }


    if (userNum < 20) {
        document.write('Your number is ' + lowNum[userNum])
    }

    else if (userNum >= 20){
        const tensDigit = Math.floor(userNum/10)
        const onesDigit  = (userNum%10)
        document.write('Your number is ' + highNum[tensDigit] +  '-' + lowNum[onesDigit])
    }

}   
