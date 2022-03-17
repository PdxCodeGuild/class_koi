#coins = [
  #  ('half-dollar', 50),
  #  ('quarter', 25),
   # ('dime', 10),
   # ('nickel', 5),
   # ('penny', 1)
#]

total = input("Please enter a dollar amount" )
total = float(total)
print (total)


total = total // .25
print (f"This uses {total} quarters")
total = total / .10
print (f"This uses {total} dimes")
total = total / .05
print (f"This uses {total} nickels")
total = total /.01
print (f"This uses {total} pennies")


#doesthiswork = total / coins[0][1]
#print (doesthiswork)
