
answer = input ("Please choose a number: ") # Requestes user input a number


# basic dictionary 
numdict = {
 1 : "one",
 2 : "two",
 3 : "three",
 4 : "four",
 5 : "five",
 6 : "six",
 7 : "seven" ,
 8 : "eight",
 9 : "nine",
 10 : "ten",
 20 : "twenty",
 30 : "thirty",
 40 : "fourty" ,  
 50 : "fifty",
 60 : "sixty",
 70 : "seventy",
 80 : "eighty", 
 90 : "ninety",
 100: "one hundred",
    
}
answer = input ("Please choose a number: ") # Requestes user input a number
new_answer = int(answer)

# if key == user input then print value of that key. 
if new_answer in numdict:
        print(numdict[new_answer])
else:
        print ("Out of dictionary bounds")