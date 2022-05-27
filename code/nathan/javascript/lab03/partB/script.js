

function convertToChange(input)
{
    let coins = [
        ['half-dollar', 50],
        ['quarter', 25],
        ['dime', 10],
        ['nickle', 5],
        ['penny', 1]
    ];
    let newArray = []
    input = parseFloat(input)
    input *= 100;

    for(let coin of coins)
    {
        let temp = Math.floor(input / coin[1]);
        console.log(temp + " " + coin[0])
        newArray.push(temp + " " + coin[0])
        input -= temp * coin[1]
    }
    console.log(newArray)
    return newArray
}

// let userInput = prompt("Enter the amount that you'd like to convert");
const userInput = document.getElementById('user_input')
const userResult = document.getElementById('user_result')
const submitButton = document.getElementById('user_input-submit')

submitButton.addEventListener('click', function(event){
    userResult.innerText = convertToChange(userInput.value);
    event.preventDefault()
})