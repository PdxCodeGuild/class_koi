#----- Version 1 -----#

class ATM:
    def __init__(self, balance = 0, interest_rate = 0.1):
        
        self.balance = balance
        self.interest_rate = interest_rate
        #----- Version 2 -----#
        self.transactions = []

    def check_balance(self):
        """return the account balance"""
        
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""

        self.balance += amount
        self.transactions.append(f'\nYou deposited ${amount}.')


    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""

        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        
        self.balance -= amount
        self.transactions.append(f'\nYou withdrew ${amount}')

        return amount

    def calc_interest(self):
        """calculate and return interest gained on account"""

        return round(self.balance * self.interest_rate,2)

    #----- Version 2 -----#
    def print_transactions(self):

        transaction_statement = ''

        if self.transactions == []:
            print('\n There are no transactions on record.')
        else:
            for transaction in self.transactions:
                transaction_statement += f'{transaction}'
            return transaction_statement



atm = ATM()  # create an instance of our class
print('\nWelcome to M0$$ Bank!')

while True:
    command = input('''\nEnter a command:\n 
    balance  - access the current balance
    deposit  - deposit money
    withdraw - withdraw money
    interest - access accumulated interest
    transactions - access your transaction history
    help     - instructions
    exit     - exit the programm\n
    ''')

    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'\nYour balance is ${balance}.')
    
    elif command == 'deposit':
        amount = float(input('\nHow much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print('-'*25)
        print(f'\nDeposited ${amount}\n')
        print('-'*25)

    elif command == 'withdraw':
        amount = float(input('\nHow much would you like to withdraw? '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print('-'*25)
            print(f'\nWithdrew ${amount}\n')
            print('-'*25)
        else:
            print('\n*$*$* Insufficient Funds *$*$*')
    
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'\nAccumulated ${amount} in interest.')
    
    #----- Version 2 -----#
    elif command == 'transactions':

        transaction_history = atm.print_transactions()
        print(f'\n---Transactions Record---\n{transaction_history}\n')
        print('-'*25)
    
    elif command == 'help':
        print('\nType following commands, typo sensitive:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - access your transaction history')
        print('exit     - exit the program')
    
    elif command == 'exit':
        print('\nThank you for banking with M0$$ Bank. Goodbye.\n')
        break
    
    else:
        print('\nCommand not recognized.')
