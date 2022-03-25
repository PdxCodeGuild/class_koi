# Version 1

user_input = input("Please enter your 16 digit card number with no spaces: ")

# create a function to for cc validation
def cc_check(card):
    num_list = list(card) # Create a list 
    check_digit = num_list[14:15:]# Store check digit
    print (check_digit)
    num_list.reverse() # reverse the list
    every_other = num_list[::2] # get every other element and add to new list 
    every_other = [int(i) for i in every_other] #turn list items to integers
    doubled_list = [num * 2 for num in every_other]
    print (doubled_list)
    # for loop to find integers larger then 9 to subtract 9
    counter = 0
    for num in doubled_list:
        if num >= 9:
            num -= 9 
            doubled_list[counter] = num
        counter += 1
    print (doubled_list)
    # sum all values on list
    all_values = sum(doubled_list)
    print (all_values)
    all_values = str(all_values)
    validation_digit = all_values[1]
    if validation_digit == check_digit:
        return True
    else:
        return False 
        
results = cc_check (user_input)       
if results == True:
    print("This credit card is valid")
else:
    print ("This credit card is invalid")