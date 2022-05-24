// declare converter objects
onesNames = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
}

tensNames = {
    0:'',
    1:'ten',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}

teensNames = {
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

// ask for a number
let numberDigit = prompt('Please enter a number (0-999): ')

// declare variable for response
let numberPhrase = ''

// handle "0" input
if (numberDigit == 0) {
    numberPhrase = 'zero'
} else {
    // handle hundreds
    if (numberDigit > 99) {
        numberPhrase += onesNames[numberDigit[0]] + '-hundred '
        // subtract hundreds from input
        numberDigit -= numberDigit[0] * 100
    }
    // handle tens that are not teens
    if (numberDigit > 19) {
        numberPhrase += tensNames[numberDigit.toString()[0]]
        // subtract tens from input
        numberDigit -= numberDigit.toString()[0] * 10
        // add a hyphen if there is a non-zero ones digit remaining
        if (numberDigit) {
            numberPhrase += '-'
        }
    // handle teens
    } else if (numberDigit > 9) {
        numberPhrase += teensNames[numberDigit.toString()]
        // make variable zero to help ones handling
        numberDigit -= numberDigit
    }
    // handle ones
    if (numberDigit) {
        numberPhrase += onesNames[numberDigit]
    }
}

// display results
alert(numberPhrase)