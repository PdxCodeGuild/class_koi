answer = input ("Please choose a number: ") # Requestes user input a number
new_answer = int(answer)

value = int(answer)
ones_place = value % 10
print (ones_place)
tens_place = (value % 100) // 10 
print (tens_place)
hundreds_place = value // 100
print (hundreds_place)



ones = {
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
teens ={
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
tens ={
 2 : "twenty",
 3 : "thirty",
 4 : "fourty" ,  
 5 : "fifty",
 6 : "sixty",
 7 : "seventy",
 8: "eighty", 
 9: "ninety",
}
hundreds ={
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


if tens_place == 0:
    print(f"Your total is {ones[ones_place]}")
elif hundreds_place >= 1:
    print(f"Your total is {hundreds[hundreds_place]} {tens[tens_place]} {ones[ones_place]}")
elif tens_place == 1:
    print(f"Your total is {teens[ones_place]}")
elif tens_place > 1 and ones_place == 0:
    print(f"Your total is {tens[tens_place]}")
elif tens_place > 1 and ones_place >= 0:
    print(f"Your total is {tens[tens_place]} {ones[ones_place]}")



