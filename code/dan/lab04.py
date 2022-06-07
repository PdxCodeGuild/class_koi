
answer = input ("Please choose a number: ") # Requestes user input a number
new_answer = int(answer)


value = int(answer)
ones = value % 10
tens = (value % 100) // 10 
hundreds = value // 100
print (f"{hundreds} hundreds {tens} tens {ones} ones")


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
 11 : "eleven",
 12 : "twelve",
 13 : "thirteen",
 14 : "fourteen",
 15 : "fifteen",
 16 : "sixteen",
 17 : "seventeen",
 18 : "eighteen",
 19 : "nineteen",
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

x = numdict[hundreds]
y = numdict[tens]
z = numdict[ones]
print (x,y,z)


# if key == user input then print value of that key. 
if new_answer in numdict:
        print(numdict[new_answer])
else:
        print ("Out of dictionary bounds")
        




# Version 2        
        
        #number text list
a_list = ['zero', 'one', 'two','three', 'four', "five",'six','seven','eight','nine',]

answer = input ("Please choose a number: ") # Requestes user input a number

value = int(answer)

for char in answer:
    char = int(char)
    print(a_list[char])
           
        
value = int(answer)
ones = value % 10
tens = (value % 100) // 10 
hundreds = value // 100
print (f"{hundreds} hundreds {tens} tens {ones} ones")
        
        