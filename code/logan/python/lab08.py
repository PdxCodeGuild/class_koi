teststring = "4556737586899855"

def conversion(string):
    # converts input string into list of ints
    int_list = []
    for character in string:
        int_list.append(int(character))
    return int_list

def doubler(x):
    doubled_int_list = []
    for int in x:
        int *= 2
        doubled_int_list.append(int)
    return doubled_int_list

# print("checks:")
int_list = conversion(teststring)
# print(int_list)
check_digit = int_list[-1]
# print(check_digit)
int_list.pop(-1)
# print(int_list)
int_list.reverse()
# print(int_list)
doubled_int_list = doubler(int_list)
# print(doubled_int_list)
print(sum(doubled_int_list))