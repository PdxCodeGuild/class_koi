let cards ={ 
    "A" : 1, 
    "K" : 10,
     "Q": 10,
     "J": 10,
     "2": 2,
     "3": 3,
     "4": 4,
     "5": 5,
     "6": 6,
     "7": 7,
     "8": 8,
     "9": 9,
     "10": 10,
}

let card_1 = prompt("What is a card 1 in your hand? ")
let card_2 = prompt("What is a card 2 in your hand? ")
let card_3 = prompt("What is a card 3 in your hand? ")

let playersHand = cards[card_1] + cards[card_2] + cards[card_3]
console.log (playersHand)


if (playersHand < 17){
    alert("Hit");
}      
else if ((playersHand > 17) && (playersHand < 21)){
    alert("Stay");
}
else if (playersHand == 21){
    alert ("Blackjack!");
}
else if (playersHand > 21){
    alert("You Busted");
}


