'''
Lab 03: Make Change
'''


while True:
    try:
        dollar_amount = float(input('Enter a dollar amount: '))
        break
    except ValueError:
        print('That is not a numerical value.')

penny_amount = dollar_amount * 100

quarter = 25
dime = 10
nickel = 5
penny = 1

quarters = penny_amount // quarter # quarters
penny_amount -= quarter * quarters

dimes = penny_amount // dime # dimes
penny_amount -= dime * dimes

nickels = penny_amount // nickel #nickels
penny_amount -= nickel * nickels

pennies = penny_amount // penny # pennies

print(f'{int(quarters)} quarters, {int(dimes)} dimes, {int(nickels)} nickels, {int(pennies)} pennies')

