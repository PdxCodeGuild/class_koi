// Pick 6 Lottery Investment Calculator

function genWinners () {
    let winningNumbers = [];
    for (let i=0; i<6; i++) {
        number = Math.round(Math.random()*99);
        winningNumbers.push(number);
    }
    return winningNumbers;
};

function genPlayerNums (userLoops) {
    let playerNumbers = [];
    for (let i=0; i<userLoops; i++) {
        //generate individual set
        let singleSet = [];
        for (let i=0; i<6; i++) {
            number = Math.round(Math.random()*99);
            singleSet.push(number);
        }
        playerNumbers.push(singleSet);
    };
    return playerNumbers;
};

let payouts = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

function calcWinnings (winningNums, playerNums) {
    let winnings = 0;
    for (let i=0; i<playerNums.length; i++) {
        let matchCount = 0;
        for (let j=0; j<playerNums[i].length; j++) {
            if (winningNums[j] == playerNums[i][j]) {
                matchCount++;
            }
        }
        winnings += payouts[matchCount]
    }
    return winnings;
}


// Play the lottery
let btPlay = document.querySelector('#btPlay');
console.log(btPlay);
btPlay.onclick = function() {
    let expenses = 0;
    let balance = 0;
    let userLoops = document.querySelector('#userLoops').value;
    if (userLoops <= 100000 && userLoops >= 1) {
        expenses += userLoops * 2
        // call another function to calculate winning tix
        winningNumbers = genWinners();
        playerNumbers = genPlayerNums(userLoops);
        winnings = calcWinnings(winningNumbers, playerNumbers);
        balance = winnings - expenses;
        document.getElementById('balanceResult').innerHTML = `congratulations! you netted \$${balance}! you spent \$${expenses} and won \$${winnings}.`
    } else {
        document.getElementById('balanceResult').innerHTML = 'Please enter a number between 1 and 100000.'
    }
}