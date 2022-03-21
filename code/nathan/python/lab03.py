'''
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
'''

def versionOne():
    num = float(input("Enter a dollar amount: "))
    #halfDollars = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = num

    pennies *= 100
    #halfDollars = pennies // 50
    #pennies -= halfDollars * 50
    quarters = int(pennies // 25)
    pennies -= quarters * 25
    dimes = int(pennies // 10)
    pennies -= dimes * 10
    nickles = int(pennies // 5)
    pennies -= nickles * 5
    pennies = int(pennies)

    print(f"{quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies")
    return


# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

def versionTwo():
    num = float(input("Enter a dollar amount: "))
    num *= 100
    coins = [
        ('half-dollar', 50),
        ('quarter', 25),
        ('dime', 10),
        ('nickle', 5),
        ('penny', 1)
    ]

    for coin in coins:
        temp = int(num // coin[1])
        print(f"{temp} {coin[0]}, ")
        num -= temp * coin[1]


versionOne()
versionTwo()