# #Version 1##
# #Code##

# special = False
# d_ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
# d_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
# num_input = int(input("\nPlease input a number 0 - 99:  "))
# ones = num_input % 10
# tens = num_input // 10
# print("\n")


# def stringwriter(x):
#     if x < 10:
#         return(d_ones[ones])
#     elif x >= 20:
#         if ones == 0:
#             return(d_tens[tens]) 
#         else:
#             return(d_tens[tens] + "-" + d_ones[ones])

# ##The Specials, 0 - 19##
# if num_input == 0:
#     print("zero")
#     special = True
# elif num_input == 10:
#     print("ten")
#     special = True
# elif num_input == 11:
#     print("eleven")
#     special = True
# elif num_input == 12:
#     print("twelve")
#     special = True
# elif num_input == 13:
#     print("thirteen")
#     special = True
# elif num_input == 14:
#     print("fourteen")
#     special = True
# elif num_input == 15:
#     print("fifteen")
#     special = True
# elif num_input == 16:
#     print("sixteen")
#     special = True
# elif num_input == 17:
#     print("seventeen")
# elif num_input == 18:
#     print("eighteen")
#     special = True
# elif num_input == 19:
#     special = True
#     print("nineteen")

# if special == False:
#     print(stringwriter(num_input))

# print("\n")

##Version 2##

# Here are a bunch of variables

special = False

d_ones = {1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
}

d_tens = {
1: "ten",
2: "twenty",
3: "thirty",
4: "forty",
5: "fifty",
6: "sixty",
7: "seventy",
8: "eighty",
9: "ninety",
}

d_hundreds = {
1: "one hundred", 
2: "two hundred", 
3: "three hundred", 
4: "four hundred", 
5: "five hundred", 
6: "six hundred", 
7: "seven hundred", 
8: "eight hundred", 
9: "nine hundred",
}

d_special = {
10: "ten", 
11: "eleven", 
12: "twelve", 
13: "thirteen", 
14: "fourteen", 
15: "fifteen", 
16: "sixteen", 
17: "seventeen", 
18: "eighteen", 
19: "nineteen"}

while True:
    try: 
        num_input = int(input("\nPlease input a number 0 - 999:  "))
        if len(str(num_input)) <= 3:
            break
        else:
            print("Invalid input.  Please input a number less than 1000.")
    except:
        print("Invalid input.  Please input a number less than 1000.")

snum_input = str(num_input)
ones = num_input % 10
tens = num_input // 10
hundreds = num_input // 100
print("\n")

# This returns #s that aren't special(0, 11-19) and less than 100 as a string.
def stringwriter(x):
    if x < 10:
        return(d_ones[ones])
    elif x >= 20:
        if ones == 0:
            return(d_tens[tens]) 
        else:
            return(d_tens[tens] + "-" + d_ones[ones])

# This returns numbers that aren't special (0, 11-19) and >= 100 as a string.
def superstringwriter():
    special_check = int(snum_input[1] + snum_input[2])
    if (snum_input[1] == "0" and snum_input[2] == "0"):
        return(d_hundreds[hundreds])
    elif (snum_input[1] != "0" and snum_input[2] == "0"):
        return(d_hundreds[hundreds] + " and " + d_tens[int(snum_input[1])])
    elif (snum_input[1] == "0" and snum_input[2] != "0"):
        return(d_hundreds[hundreds]) + " and " + d_ones[int(snum_input[2])]
    elif special_check in d_special:
        return(d_hundreds[hundreds] + " and " + d_special[special_check])
    else:
        return(d_hundreds[hundreds] + " and " + d_tens[int(snum_input[1])] + "-" + d_ones[ones])

## The Specials 0, 10 - 19 -- these have no good, regular convention for generation##
if num_input == 0:
    print("zero")
    special = True
elif num_input == 10:
    print("ten")
    special = True
elif num_input == 11:
    print("eleven")
    special = True
elif num_input == 12:
    print("twelve")
    special = True
elif num_input == 13:
    print("thirteen")
    special = True
elif num_input == 14:
    print("fourteen")
    special = True
elif num_input == 15:
    print("fifteen")
    special = True
elif num_input == 16:
    print("sixteen")
    special = True
elif num_input == 17:
    print("seventeen")
elif num_input == 18:
    print("eighteen")
    special = True
elif num_input == 19:
    special = True
    print("nineteen")

if special == False:
    if num_input < 100:
        print(stringwriter(num_input))
    else:
        print(superstringwriter())

print("\n")