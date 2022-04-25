coins = [
   ('half-dollar', 50),
    ('quarter', 25),
   ('dime', 10),
   ('nickel', 5),
   ('penny', 1),
]

#doesthiswork = total / coins[0][1]
#print (doesthiswork)


amount = input("Please enter a dollar amount" )
amount = float(amount)
print (amount) 



quarters = amount // .25 
dimes = amount // .10
nickels = amount // .05
pennies = amount  / .01
print (f"This uses {quarters} quarters, {dimes} dimes , {nickels} nickels , {pennies} pennies") 
