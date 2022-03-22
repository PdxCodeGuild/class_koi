# Lab 8: Credit Card Validation
# Mitch Chapman


def credit_valicator(card_num_str: str):

    card_num_list = [int(num) for num in card_num_str]
    
    check_digit = str(card_num_list.pop(-1))
    
    card_num_list.reverse()
    
    for i, num in enumerate(card_num_list):
        if i % 2 == 0:
            card_num_list[i] = num * 2

    for i, num in enumerate(card_num_list):
        if num > 9:    
            card_num_list[i] = num - 9
        
    determined_number = str(sum(card_num_list))[1]
            
    if determined_number == check_digit:
        return "Valid"
    else:
        return "Invalid"
    



print(credit_valicator("4556737586899855"))








