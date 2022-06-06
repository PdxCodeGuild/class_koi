// #  *'-.-'*'-.-'*'-.-'*'--'*
// #     Project: Python 
// #   Lab 2: Average Numbers 
// #       Version: 1.0
// #   Author: Shaine Warren
// #   Email: mwarren86@gmail.com
// #       Date: Mar, 2022
// # *'-.-'*'-.-'*'-.-'*'--'*


document.getElementById("theButton").onclick = function(){
    let userInput = document.getElementById("textBox").value;
    
    let userNums = userInput.split("-").map(Number);
    const nums = userNums;

    let sum = 0;

    for (let num of nums)
        sum += num;
    
const total = sum/nums.length;
document.write('Numbers Added: ' + nums + '<br/>'); 
document.write('Average: ' + total.toFixed(4));
}
