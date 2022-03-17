
#----- Version 1 -----#
print('\nMaking Change\n')

user_amount_in = float(input('\nEnter a dollar amount:\n'))

user_amount_out = user_amount_in

print('_______________________________')

print('QUARTERS')
user_amount_floord_q = round(user_amount_out//.25)
print(user_amount_floord_q)
user_amount_out = round(user_amount_out%.25,2)
print(user_amount_out)

print('_______________________________')

print('DIMES')
user_amount_floord_d = round(user_amount_out//.10)
print(user_amount_floord_d)
user_amount_out = round(user_amount_out%.10,2)
print(user_amount_out)

print('_______________________________')

print('NICKELS')
user_amount_floord_n = round(user_amount_out//.05)
print(user_amount_floord_n)
user_amount_out = round(user_amount_out%.05,2)
print(user_amount_out)

print('_______________________________')

print('PENNIES')
user_amount_floord_p = round(user_amount_out//.01)
print(user_amount_floord_p)
user_amount_out = round(user_amount_out%.01,2)
print(user_amount_out)

print(f"""
\n${user_amount_in} is : {user_amount_floord_q} quarter(s), {user_amount_floord_d} dime(s), {user_amount_floord_n} nickel(s), and {user_amount_floord_p} pennie(s)\n""")