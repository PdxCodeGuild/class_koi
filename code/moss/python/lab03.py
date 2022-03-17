
print('\nMaking Change\n')

user_amount = float(input('\nEnter a dollar amount:\n'))



penny_calc = (user_amount*100)
amount = penny_calc//.01

nickel_calc = round(user_amount//.05)
user_amount = user_amount%0.5

dime_calc = round(user_amount//.10)
user_amount = user_amount%0.10

quarters_calc = round(user_amount//.25)
user_amount = user_amount%0.25





print(
f"""
\npennies: {amount},
nickels: {nickel_calc},
dimes: {dime_calc},
quarters: {quarters_calc},
""")


