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

    let dollarAmount = userInput;

    const dollarConvert = (dollarAmount * 100);

    const quarters = Math.floor(dollarConvert/25)

    const dimes = Math.floor((dollarConvert%25)/10)

    const nickles = Math.floor(((dollarConvert%25)%10)/5)

    const pennies = Math.floor((((dollarConvert%25)%10)%5)/1)

    document.write(quarters + ' quarters,' + dimes + ' dimes,' + nickles + ' nickles,' + pennies + ' pennies')

}

