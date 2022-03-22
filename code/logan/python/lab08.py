## Lab 08 ##
## Code ##

# teststring = "4556737586899855" 
# This was for testing the program.

while True:
    try:
        card = input("\nInput your card number:...")
        int(card)
        break
    except:
        print("Invalid input.  Please input a number.")


def conversion(string):
# Converts input string into list of ints
    int_list = []
    for character in string:
        int_list.append(int(character))
    return int_list

def doubler(x):
# Doubles first element and every other element after
    counter = 0
    doubled_int_list = []
    for int in x:
        if counter % 2 == 0:
            int *= 2
            doubled_int_list.append(int)
            counter += 1
        else:
            doubled_int_list.append(int)
            counter += 1
    return doubled_int_list

def nine_eliminator(x):
# Subtracts anything > 9 by 9
    nines_gone = []
    for int in x:
        if int > 9:
            int = int - 9
            nines_gone.append(int)
        else:
            nines_gone.append(int)
    return nines_gone

def second_grabber(x):
# grabs the second digit of an integer
    x = str(x)
    x = x[1]
    return int(x)

## The various checks here can be uncommented to see the numbers transform.
# print("checks:")
## Only uncomment the next line if you're running the teststring.
# int_list = conversion(teststring)
int_list = conversion(card)
# print(int_list)
check_digit = int_list[-1]
# print(check_digit)
int_list.pop(-1)
# print(int_list)
int_list.reverse()
# print(int_list)
int_list = doubler(int_list)
# print(int_list)
int_list = nine_eliminator(int_list)
# print(int_list)
summed = sum(int_list)
# print(summed)
second_digit = second_grabber(summed)
# print(second_digit)

# Checks validity

if second_digit == check_digit:
    valid = True
else:
    valid = False

# Output

print(f"""
Valid Number?...{valid}
""")
