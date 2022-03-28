'''
PDX Code Guild - Class Koi
Lab 08 - Credit Card Validation
Matt Walsh
'''


# check to see if a credit card number is valid
def check_cc(num):
    # convert the number to a list of numbers
    num = list(num)
    # remove the last digit and store as an integer
    check_digit = int(num.pop(-1))
    # reverse the order of the list
    num.reverse()
    # variable to hold sum of processed num list
    num_sum = 0
    # iterate through numbers in list
    for x in range(15):
        # convert each to integers
        num[x] = int(num[x])
        # for every other number, multiply by 2
        if x % 2 == 0:
            num[x] *= 2
            # if the result is over 9, subtract 9
            if num[x] > 9:
                num[x] -= 9
        num_sum += num[x]
    # compare the second digit of num_sum to check_digit
    if num_sum % 10 == check_digit:
        return 'Valid!'
    else:
        return 'Invalid: this number did not pass the verfication check.'

while True:
    # prompt for user input
    cc_num = input('Please enter a Credit Card number: ')
    try:
        # check if the input is only digits
        int_check = int(cc_num)
        # check if the input is 16 digits long and display results
        if len(cc_num) == 16:
            print(check_cc(cc_num))
        else:
            print('Invalid: a valid credit card number is 16 digits long.')
    except:
        print('Invalid: a valid credit card number only contains digits.')
    # ask user if they would like to try again
    while True:
        try_again = input('\nWould you like to try another number? Y or N: ')
        # assign variable to break out of nested loop
        break_out = False
        if try_again.upper() == 'N':
            # if user says no, make break_out True and break this loop
            break_out = True
            break
        elif try_again.upper() == 'Y':
            # if user says yes, break this loop with break_out still False
            break
        else:
            # if anything else is entered, ask again
            print('I didn\'t understand that.')
    # break this loop if user said no in previous loop
    if break_out == True:
        break