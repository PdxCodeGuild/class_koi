// javaScript Lab02 - Blackjack Advice
// Part B

function handValue(x, y, z){
    return (x + y + z)
}
button.addEventListener('click', function (e) {
    e.preventDefault()
    const card1Input = document.querySelector('#card1Input')
    const card1 = +card1Input.value
    const card2Input = document.querySelector('#card2Input')
    const card2 = +card2Input.value
    const card3Input = document.querySelector('#card3Input')
    const card3 = +card3Input.value
    const button = document.querySelector('#button')
    const p = document.createElement('p')
    if (handValue(card1, card2, card3) == 21) {
        output.innerText = `Blackjack!! \nYou Win!!`
    }
    else if (handValue(card1, card2, card3) > 16) {
        output.innerText = `Your hand value = ${handValue(card1, card2, card3)}\nStay`
    }
    else {
        output.innerText = `Your hand value = ${handValue(card1, card2, card3)}\nHit`
    }
    console.log(card1, card2, card3)
    console.log(handValue(card1,card2,card3))
})
