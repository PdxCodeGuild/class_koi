// javaScript Lab03 - Pick 6: Picks
// Part B

const winningsDict = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

const input = document.querySelector('#input')
const buttom = document.querySelector('#button')

let numsArray = []
function pick6(numsArray) {
    for (let i=0; i < 99; i++) {
        numsArray[i] = i + 1
    }
    numsArray.sort(() => Math.random() - 0.5)
    return numsArray.slice(0,6)
}

function numMatches(lotteryNumbers, tempTicket) {
    let matches = 0
    for (let i = 0; i < 6; i++) {
        if (lotteryNumbers[i] == tempTicket[i]) {
            matches++  
        }
    }
    return matches
}

var expenses = 0
var earnings = 0
var balance = 0
function playLottery(timesPlayed) {
    lotteryNumbers = pick6(numsArray)
    console.log(lotteryNumbers)
    let i = 0
    let matchesTemp = 0
    do {
        i++
        tempTicket = pick6(numsArray)
        // console.log(tempTicket)
        matchesTemp = numMatches(lotteryNumbers, tempTicket)
        let winnings = winningsDict[matchesTemp]
        earnings += winnings
        balance = earnings - 2
        expenses += 2
    }
    while (i < timesPlayed)
}

button.addEventListener('click', function() {
    const timesPlayed = +input.value
    playLottery(timesPlayed)
    const netProfit = (earnings-expenses)
    const roi = ((netProfit)/(expenses))
    output.innerText = `The winning lottery numbers were: ${lotteryNumbers}`
    output1.innerText = `You purchased ${timesPlayed} lottery tickets.`
    output2.innerText = `Your Return on Investment - ROI was: ${roi}`
    output3.innerText = `Your earnings were: $${earnings.toLocaleString("en-US")} Your expenses were: $${expenses.toLocaleString("en-US")}`
    // console.log(earnings.toLocaleString("en-US"))
    // console.log(expenses.toLocaleString("en-US"))
    // console.log(lotteryNumbers)
    // console.log(playLottery(timesPlayed))
})