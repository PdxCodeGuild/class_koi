# Version 1

# get 16 digit credit card input
string_input = input("Please enter your 16 digit card number with no spaces: ")
print (string_input)

#convert string to list
string_of_ints = [] # empty list to append integers 
for item in string_input: # loop though number strings convert to numbers
    item = int(item) 
    string_of_ints.append(item)
    print (string_of_ints)

# slice off the last digit
check_digit = string_of_ints[14:15:]
print (check_digit)

#reverse the list
string_of_ints.reverse()
print (string_of_ints)

# create list of every other digit
every_other_num = string_of_ints[::2]
print (every_other_num)

# double every element in list
doubled_list = [num ** 2 for num in every_other_num]
print(doubled_list)

# subtract 9 for numbers of 9
minus_nine = [num-9 for num in doubled_list if num >= 9]
print (minus_nine)

# sum all values
all_values = sum(minus_nine)
print (all_values)

# get second digit 
all_values = str(all_values)
validation_digit = all_values[1]
print (validation_digit)

# validate card logic
if validation_digit == check_digit:
    print ("This is a valid card")
else:
    print ("This card is invalid")
