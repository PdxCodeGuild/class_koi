apples = 27

apples = input('How many apples does Lisa have to sell? ')

apples = int(apples)

print(f"""

Lisa has {apples} apples.  She sells them by the dozen.

If she sells a dozen apples at a time, how many sales does she make?

And how many apples are left over?

""")



# floor division: //
# after division, rounded down to an integer

dozens_sold = apples // 12

# modulus: %
# how many are left over after floor division (like the remainder in long division)

leftover_apples = apples % 12

print(f"""
Lisa sold {dozens_sold} dozen apples.

Lisa has {leftover_apples} apples remaining.

""")
