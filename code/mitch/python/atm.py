# Lab 13: ATM
# Versions 1 and 2
# Mitch Chapman

class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_record = []


    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transaction_record.append(f"--User deposited ${amount}")

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        temp_check_value = self.balance - amount
        if temp_check_value >= 0:
            return True
        else:
            return False
        

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.transaction_record.append(f"--User withdrew ${amount}")
        return self.balance


    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = self.interest_rate * self.balance
        return interest
    
    def print_transactions(self):
        """prints a list of all transactions user has completed"""
        print("\n".join(self.transaction_record))