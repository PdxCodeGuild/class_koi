'''
PDX Code Guild - Class Koi
Lab 13 - ATM
Matt Walsh
'''


# Version 1
'''
class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance >= amount:
            return True
        return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = self.balance * self.interest_rate
        return interest


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
'''


# Version 2

class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = ''

    def check_balance(self):
        """return the account balance"""
        self.transactions += f'\nchecked balance: {self.balance}'
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.transactions += f'\ndeposited {amount}'
        self.balance += amount

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance >= amount:
            return True
        self.transactions += f'\nfailed to withdraw {amount}'
        return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.transactions += f'\nwithdrew {amount}'

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = self.balance * self.interest_rate
        self.transactions += f'\naccumulated {interest} in interest'
        return interest

    def print_transactions(self):
        """display recent transactions"""
        return self.transactions

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
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
        transactions = atm.print_transactions()
        print(f'Recent transactions:{transactions}')
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('transactions - display transactions')
        print('exit         - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')