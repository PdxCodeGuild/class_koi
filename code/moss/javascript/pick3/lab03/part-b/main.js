let cardInput = document.getElementById("card-select")
let addCardButton = document.getElementById("add-card")
let adviseButton = document.getElementById("advice")
let cardHand = document.getElementById("card-hand")
let output = document.getElementById("output")
let advisor = document.getElementById("advisor")

cardHandList = []

addCardButton.addEventListener("click", function() {
    
    let card_choice = cardInput.value
    cardHandList.push(card_choice)
    cardHand.innerText = `Hand : ${cardHandList}`
    console.log(`${cardHandList} is the player's hand`)
})

adviseButton.addEventListener("click", function() {
        
    function sum(numbers) {
        total_score = 0
        for (i of numbers) {
            total_score += parseInt(i)
        }
        return total_score
    }

    let result = sum(cardHandList)
    console.log(`${result} is the score`)



    if (result <= 17) {
        output.innerText = `Your score is : ${result}`
        advisor.innerText = `HIT!`
    }

    else if (result >= 17 && result < 21) {
        output.innerText = `Your score is : ${result}`
        advisor.innerText = `STAY`
    }

    else if (result === 21 ) {
        output.innerText = `Your score is : ${result}`
        advisor.innerText = `BLACKJACK!`
    }

    else if (result > 21) {
        output.innerText = `Your score is : ${result}`
        advisor.innerText = `ALREADY BUSTED!`
    }
})

