# # Version 1

# #Please enter a dollar amount
dollar_amount = float(input('Please enter a dollar amount '))

# #convert to pennies
pennies = dollar_amount * 100

leftover_dimes = float(0)
leftover_nickles = float(0)
leftover_quarters = float(0)
dime = 0
nickle = 0
quarter = 0

#convert to quarters, dime, nickel, pennies
if pennies >= 25:
    quarter = pennies // 25
    pennies = pennies - (quarter * 25)
    leftover_quarters = quarter % 25
    print(pennies)

if pennies >= 10:
    dime = pennies // 10
    pennies = pennies - (dime * 10)
    leftover_dimes = leftover_quarters % 10
    print(pennies)

if pennies >= 5:
    nickle = pennies // 5
    pennies = pennies - (nickle * 5)
    leftover_nickles = leftover_dimes % 5
    print(pennies)


print(f'You have {int(quarter)} quarters. {int(dime)} dimes, {int(nickle)} nickles and {int(pennies)} pennies')


# Version 2
#Please enter a dollar amount
dollar_amount = float(input('Please enter a dollar amount '))

#convert to pennies
pennies = dollar_amount * 100

leftover_dimes = float(0)
leftover_nickles = float(0)
leftover_quarters = float(0)
dime = 0
nickle = 0
quarter = 0

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

print(pennies)

if pennies >= coins[0][1]:
    half_dollar = pennies // coins[0][1]
    pennies = pennies - (half_dollar * coins[0][1])
    leftover_quarters = half_dollar % coins[0][1]
    print(pennies)


if pennies >= coins[1][1]:
    quarter = pennies // coins[1][1]
    pennies = pennies - (quarter * coins[1][1])
    leftover_quarters = quarter % coins[1][1]
    print(pennies)

if pennies >= coins[2][1]:
    dime = pennies // coins[2][1]
    pennies = pennies - (dime * coins[2][1])
    leftover_dimes = leftover_quarters % coins[2][1]
    print(pennies)

if pennies >= coins[3][1]:
    nickle = pennies // coins[3][1]
    pennies = pennies - (nickle * coins[3][1])
    leftover_nickles = leftover_dimes % coins[3][1]
    print(pennies)

print(f'You have {int(half_dollar)} half dollars {int(quarter)} quarters. {int(dime)} dimes, {int(nickle)} nickles and {int(pennies)} pennies')