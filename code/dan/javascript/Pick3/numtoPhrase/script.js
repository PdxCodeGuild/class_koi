let someNum = prompt("Please enter a number 0-999")
console.log(someNum)

let ones = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven" ,
    8 : "eight",
    9 : "nine",
     
   }
   let teens ={
    0 : "ten",
    1 : "eleven",
    2 : "twelve",
    3 : "thirteen",
    4 : "fourteen",
    5 : "fifteen",
    6 : "sixteen",
    7 : "seventeen",
    8 : "eighteen",
    9 : "nineteen",
   }
   let tens ={
    0 : "zero" 
    2 : "twenty",
    3 : "thirty",
    4 : "fourty" ,  
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8: "eighty", 
    9: "ninety",
   }
   let hundreds ={
    1: "one hundred",
    2 : "two hundred",
    3 : "three hundred",
    4 : "four hundred" ,  
    5 : "five hundred",
    6 : "six hundred",
    7 : "seven hundred",
    8: "eight hundred", 
    9: "nine hundred",
}
   

let onesDigit = someNum[0]
let tensDigit = someNum[1]
let hundredsDigit = someNum[2]


console.log(`This is ${hundreds[hundredsDigit]} ${tens[tensDigit]} ${ones[onesDigit]}`)
