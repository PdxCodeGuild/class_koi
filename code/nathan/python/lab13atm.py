class ATM:
    def __init__(self, balance=0, interest_rate=0.1, transations = []):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transactions.append(f"User deposited {amount}")
        return self.balance

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if(self.balance >= amount):
            return True
        return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        if(self.check_withdrawal(amount)):
            self.balance -= amount
            self.transactions.append(f"User withdrew {amount}")
            return amount
        print("Not enough funds")
        return 0

    def calc_interest(self):
        """calculate and return interest gained on account"""
        return self.balance * self.interest_rate

    def print_transactions(self):
        for i in self.transactions:
            print(i)