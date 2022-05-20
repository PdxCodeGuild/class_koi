// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // declare converter objects
            onesNames: {
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
            },
            tensNames: {
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
            },
            teensNames: {
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
            },
            // set up input and output variables
            numberDigit: '',
            numberPhrase: '',
        }
    },
    methods: {
        // method for converting numbers to phrase
        convertNum () {
            // assign input number to different variable for manipulation
            let numberDigitConvert = this.numberDigit
            // clear result variable on every run
            this.numberPhrase = ''
            // give an error and reset input if it exceeds 999
            if (this.numberDigit > 999) {
                this.numberPhrase = 'Please enter a number from 0-999.'
                this.numberDigit = ''
            } else {
                // handle "0" input
                if (numberDigitConvert == 0) {
                    this.numberPhrase = 'zero'
                } else {
                    // handle hundreds
                    if (numberDigitConvert > 99) {
                        this.numberPhrase += this.onesNames[numberDigitConvert[0]] + '-hundred '
                        // subtract hundreds from input
                        numberDigitConvert -= numberDigitConvert[0] * 100
                    }
                    // handle tens that are not teens
                    if (numberDigitConvert > 19) {
                        this.numberPhrase += this.tensNames[numberDigitConvert.toString()[0]]
                        // subtract tens from input
                        numberDigitConvert -= numberDigitConvert.toString()[0] * 10
                        // add a hyphen if there is a non-zero ones digit remaining
                        if (numberDigitConvert) {
                            this.numberPhrase += '-'
                        }
                    // handle teens
                    } else if (numberDigitConvert > 9) {
                        this.numberPhrase += this.teensNames[numberDigitConvert.toString()]
                        // make variable zero to help ones handling
                        numberDigitConvert -= numberDigitConvert
                    }
                    // handle ones
                    if (numberDigitConvert) {
                        this.numberPhrase += this.onesNames[numberDigitConvert]
                    }
                }
            }
        }
    }
}).mount('#app')

