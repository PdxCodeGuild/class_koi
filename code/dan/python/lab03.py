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
amount = float(amount) * 100
print (amount) 



quarters = amount // 25 
amount %= 25
dimes = amount // 10
amount %= 10
nickels = amount // 5
amount %= 5
pennies = amount  / 1
print (f"This uses {quarters} quarters, {dimes} dimes , {nickels} nickels , {pennies} pennies") 
