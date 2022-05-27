

function convertToChange(input)
{
    let coins = [
        ['half-dollar', 50],
        ['quarter', 25],
        ['dime', 10],
        ['nickle', 5],
        ['penny', 1]
    ];

    input *= 100;

    for(let coin of coins)
    {
        let temp = Math.floor(input / coin[1]);
        console.log(temp + " " + coin[0])
        input -= temp * coin[1]
    }
}

let userInput = prompt("Enter the amount that you'd like to convert");
convertToChange(userInput);