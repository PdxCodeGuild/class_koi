# Lab 3: Make Change
# Mitch Chapman


requested_value = int(float(input("Enter a dollar ammount: ")) * 100)

statement = []

if requested_value // 25:
    if requested_value // 25 == 1:
        statement.append(f"{requested_value//25} quarter")
    else:
        statement.append(f"{requested_value//25} quarters")
    requested_value = requested_value % 25

if requested_value // 10:
    if requested_value // 10 == 1:
        statement.append(f"{requested_value//10} dime")
    else:
        statement.append(f"{requested_value//10} dimes")
    requested_value = requested_value % 10
    
if requested_value // 5:
    if requested_value // 5 == 1:
        statement.append(f"{requested_value//5} nickle")
    else:
        statement.append(f"{requested_value//5} nickles")
    requested_value = requested_value % 5

if requested_value:
    if requested_value == 1:
        statement.append(f"{requested_value} penny")
    else:
        statement.append(f"{requested_value} pennies")



print(", ".join(statement))










