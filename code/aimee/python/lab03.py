# lab03, ver 1 ---- #

dollar_amount = input('Enter the dollar amount: ')
dollar_amount = float(dollar_amount)
total_pennies = dollar_amount * 100
#print(total_pennies)

# dividing to get # of quarters
quarters = total_pennies // 25
# remaining number left after quarters
remainder_1 = total_pennies % 25 # = 11
# dividing to get # of dimes from remainder
dimes = remainder_1 // 10
# getting remaining number after dimes
remainder_2 = remainder_1 % 10
nickels = remainder_2 // 5
remainder_3 = remainder_2 % 5
pennies = remainder_3 // 1

print(f'{quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s), and {pennies} penny(s)')

# ver 2 ---- #

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]




