// javaScript Lab02 - Blackjack Advice

const possibleCards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

const cardValue = {
    'A1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A11': 11,
}

const cardName = {
    'A1': 'Ace',
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    'A11': 'Ace',
    0 : 0
}

var newline = "\n"
let card1Input = prompt("What's your first card?" + newline + "Possible card inputs: "+possibleCards)
let card1Upper = card1Input.toUpperCase()
console.log(card1Upper, typeof card1Upper)

if (card1Upper === 'A')
{
    let choice
    do{
        choice = prompt("Would you like to play your Ace as an 11 or 1:")
        if (choice === '11')
        {
            var card1 = 'A11'
        }
        else if (choice === '1')
        {
            var card1 = 'A1'
        }
    }
    while (!(choice == '1' || choice == '11'))
}
else{
    var card1 = card1Upper
}
console.log("card1", card1, "value=", cardValue[card1], "name=", cardName[card1])

let card2Input = prompt("What's your second card?" + newline + "Possible card inputs: "+possibleCards)
let card2Upper = card2Input.toUpperCase()
console.log(card2Upper, typeof card2Upper)

if (card2Upper === 'A')
{
    if (cardValue[card1] < 11)
    {
        let choice
        do{
            choice = prompt("Your 1st card was an " + cardName[card1] + " with a value of " + cardValue[card1]+"\nWould you like to play this Ace as an 11 or 1:")
            if (choice === '11')
            {
                var card2 = 'A11'
                console.log(card2, typeof card2)
            }
            else if (choice === '1')
            {
                var card2 = 'A11'
                console.log(card2, typeof card2)
            }
        }
        while (!(choice == '1' || choice == '11'))
    }
    else if (card2Upper === 'A'){
        var card2 = 'A1'
    }
}
else{
    var card2 = card2Upper
}
console.log("card2", card2, "value=", cardValue[card2], "name=", cardName[card1])

function handValue2Cards(x, y) {
    x=cardValue[card1]
    y=cardValue[card2]
    return x + y
}
var handValue2 = handValue2Cards(card1, card2)
console.log('2-cards='+handValue2)

function handValue3Cards(x, y, z) {
    x=cardValue[card1]
    y=cardValue[card2]
    z=cardValue[card3]
    return x + y + z
}


let card3Input
if (handValue2 === 21) {
    alert('You have 21, Blackjack! \nYou Win!!')
}
else if (handValue2 > 16) {
    alert('You have '+handValue2+ '\nYou should Stay')
}
else {
    alert('Your 2-card hand = '+handValue2+ '\nYou should Hit')
    card3Input = prompt("What's your 3rd card"+newline+"Possible card inputs: "+possibleCards).toUpperCase()
    if (card3Input === 'A' && (handValue2Cards(card1, card2) < 10)) 
    {
        choice = prompt("Your 1st two cards ="+handValue2Cards(card1, card2)+"\nWould you like to play this Ace as an 11 or 1:")
        do{
        if (choice === '11')
            {
                var card3 = 'A11'
                console.log(card3, typeof card3)
            }
            else if (choice === '1')
            {
                var card3 = 'A1'
                console.log(card3, typeof card3)
            }
        }
        while (!(choice == '1' || choice == '11'))
    } 
    else {
        var card3 = card3Input
    }
    var handValue3 = handValue3Cards(card1, card2, card3)
    console.log("3-cards="+handValue3)
}

if (handValue2 === 21){
    alert('Congratulations!!')
}
else if (handValue2 > 16){
    alert('Well Done on your Stay') 
}
else if (handValue3 === 21) {
    alert('You have 21, Blackjack! \nYou Win!!')
}
else if (handValue3 < 17){
    alert('You have '+handValue3+'\nYou should Hit')
}
else if (handValue3 < 21){
    alert('You have '+handValue3+'\nYou should Stay')
}
else {
    alert('You have '+handValue3+'/nYou Already Busted. \nYou Lost!!')
}



//console.log(card1, typeof card1)
