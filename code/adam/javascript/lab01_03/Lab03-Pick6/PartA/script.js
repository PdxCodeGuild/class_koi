// Lab 03 - Pick 6 Lottery

const winningsDict = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

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

const timesPlayed = +prompt('How many times will you play the Lottery?')

playLottery(timesPlayed)
const netProfit = (earnings-expenses)
const roi = ((netProfit)/(expenses))

alert('You played the lottery '+timesPlayed+' times \nThe ROI was '+roi+'\nEarnings = $'+earnings+'\nExpenses = $'+expenses+'\nNet Profit = $'+netProfit)



