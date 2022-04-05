# Lab 13 - ATM

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

class ATM:
    def __init__(self, balance=0, interest_rate=0.1, transactions=''):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transactions += '\nuser deposited ' + str(amount)

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if amount < self.balance:
            return True

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.transactions += '\nuser withdrew $ ' + str(amount)
        return amount

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest_amount = round(self.balance * self.interest_rate, 2)
        return interest_amount

    def print_transactions(self):
        print(f'Below is a list of user transactions {self.transactions}')

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? $'))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like: '))
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
        print('exit         - exit the program')
        print('transactions - prints transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
