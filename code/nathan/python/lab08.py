
def card_Validation(card_Number):
    new_Card_Number = []
    check_Digit = 0
    sum_Nums = 0

    # Convert the input string into a list of ints
    for i in card_Number:
        new_Card_Number.append(int(i))

    # Slice off the last digit. That is the check digit.
    check_Digit = new_Card_Number.pop(-1)
    # Reverse the digits.

    new_Card_Number.reverse()
    # Double every other element in the reversed list.
    for i in new_Card_Number:
        i *= 2
    # Subtract nine from numbers over nine.
        if(i > 9):
            i -= 9

    # Sum all values.
    sum_Nums = sum(new_Card_Number)

    # Take the second digit of that sum.
    sum_Nums %= 10

    # If that matches the check digit, the whole card number is valid.
    if(sum_Nums == check_Digit):
        return True
    
    return False

def card_Validation_With_Spaces(card_Number):
    check_Digit = 0
    sum_Nums = 0

    # Convert the input string into a list of ints
    card_Number = card_Number.split(' ')

    # Slice off the last digit. That is the check digit.
    check_Digit = int(card_Number.pop(-1))

    # Reverse the digits.
    card_Number.reverse()
    # Double every other element in the reversed list.
    for i in card_Number:
        i = int(i)
        i *= 2
    # Subtract nine from numbers over nine.
        if(i > 9):
            i -= 9

    # Sum all values.
    for i in card_Number:
        sum_Nums += int(i)

    # Take the second digit of that sum.
    sum_Nums %= 10

    # If that matches the check digit, the whole card number is valid.
    if(sum_Nums == check_Digit):
        return True
    
    return False

print(card_Validation('4556737586899855'))
print(card_Validation_With_Spaces('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'))