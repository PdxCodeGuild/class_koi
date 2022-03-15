## Version 1 ##
## Code ##

# running_sum = 0
# numlist = [5, 0, 8, 3, 4, 1, 6]

# for x in numlist:
#     running_sum += x
# print(f"\nAverage is: {running_sum / len(numlist)}.\n")


## Version 2 ##
## Code ##
# No code for invalid input, let me know if it needs to be added!

numlist = []
running_sum = 0

while True:
    num_add = input("\nPlease enter a number, or 'done' to quit:  ")
    if num_add == "done":
        break
    else:
        numlist.append(int(num_add))

for x in numlist:
    running_sum += x
print(f"\nAverage is {running_sum / len(numlist)}.\n")