'''
Optional Lab: Simple Calculator

-Version 2: use a REPL to allow the user 
 to keep doing calculations until entering 'done'
'''

def simp_calc(operation, num_1, num_2):
    if operation == '+':
        result = num_1 + num_2
        return result
    elif operation == '-':
        result = num_1 - num_2
        return result
    elif operation == '*':
        result = num_1 * num_2
        return result
    elif operation == '/':
        result = num_1 / num_2
        return result

while True:
    user_operation = input('What is the operation you would like to perform? (+, -, *, /, done) ')
    
    if user_operation == 'done':
        break
    
    user_num_1 = float(input('What is the first number? '))
    user_num_2 = float(input('What is the second number? '))

    user_result = simp_calc(user_operation, user_num_1, user_num_2)

    print(user_num_1, user_operation, user_num_1, '=', user_result)
