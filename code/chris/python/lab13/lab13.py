'''
Lab 13: ATM
- Fill in the methods for the ATM class

- I did not authenticate user entries so you can go negative
'''

class ATM:
    '''updates a balance and tracks deposits and withdrawals'''

    transactions = [] # version 2

    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        '''return the account balance'''
        return atm.balance
    
    def deposit(self, amount):
        '''deposit a given amount into account'''
        atm.balance += amount
        atm.transactions.append(f'Deposited ${amount}') # version 2
    
    def check_withdrawal(self, amount):
        '''return True if account has enough funds to withdraw given amount'''
        if atm.balance > amount:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        '''withdraw given amount from account and return that amount'''
        if atm.check_withdrawal(amount) == True:
            self.balance -= amount
            self.transactions.append(f'Withdrew ${amount}.') # version 2
        else:
            print("Insufficient funds.")
    
    def calc_interest(self):
        '''calculate and return interest gained on account'''
        self.interest = self.balance * self.interest_rate
        return self.interest
    
    def print_transactions(self): # version 2
        for transaction in self.transactions:
            print(transaction)
    
atm = ATM() # create an instance of our class
print("Welcome to the ATM")

while True:
    command = input('Enter a command (help for help): ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('transactions - list of transactions')
        print('exit         - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
    