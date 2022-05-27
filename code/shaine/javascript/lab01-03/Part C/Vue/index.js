// #  *'-.-'*'-.-'*'-.-'*'--'*
// #     Project: Python 
// #   Lab 4: Number to Phrase
// #       Version: 1.0
// #   Author: Shaine Warren
// #   Email: mwarren86@gmail.com
// #       Date: Mar, 2022
// # *'-.-'*'-.-'*'-.-'*'--'*

const app = Vue.createApp({
    data() {
        return {
            lowNum: {
                0:'zero',
                1:'one',
                2:'two',
                3:'three',
                4:'four',
                5:'five',
                6:'six',
                7:'seven',
                8:'eight',
                9:'nine',
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

            highNum: {
                2:'twenty',
                3:'thirty',
                4:'forty',
                5:'fifty', 
                6:'sixty', 
                7:'seventy', 
                8:'eighty',
                9:'ninety'
            },
            userInput: []
        }
    },
    methods: {

        numType() {
            if (this.userInput < 20) {
            document.write('Your number is ' + this.lowNum[this.userInput])
            }
            
            else if (this.userInput >= 20) {
            const tensDigit = Math.floor(this.userInput/10)
            const onesDigit  = (this.userInput%10)
            document.write('Your number is ' + this.highNum[tensDigit] +  '-' + this.lowNum[onesDigit])
            }
        }
        
    }
}) 

app.mount('#app')