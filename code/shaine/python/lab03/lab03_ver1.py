#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 3: Make Change 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


# convert a dollar amount into a number of coins. 

dollar_amount = float(input('Enter a dollar amount: '))

dollar_convert = dollar_amount*100

quarters = int(dollar_convert//25)

dimes = int((dollar_convert%25)//10)

nickles = int(((dollar_convert%25)%10)//5)

pennies = int((((dollar_convert%25)%10)%5)//1)

print(f'{quarters} quarters, {dimes} dime, {nickles} nickel, {pennies} pennies')

