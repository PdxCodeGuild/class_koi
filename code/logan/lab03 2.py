##Version 1##
##Code##

dollar_amount = input("\nPlease enter a dollar amount as a decimal number:  ")
dollar_adj = float(dollar_amount) * 100

quarters = (dollar_adj // 25)
running_total = (dollar_adj % 25)
dimes = running_total // 10
running_total = running_total % 10
nickels = running_total // 5
pennies = running_total % 5

print(f"\n That's {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.\n")