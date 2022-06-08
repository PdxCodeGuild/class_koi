

class Account
{
    constructor(balance = 0, interestRate = 0.1, transactions = [])
    {
        this.balance = balance;
        this.interestRate = interestRate;
        this.transactions = transactions;
    }

    checkBalance()
    {
        return this.balance;
    }

    deposit(amount)
    {
        this.balance += amount;
        this.transactions.push("User deposited " + amount);
        return this.balance;
    }

    checkWithdrawal(amount)
    {
        if(this.balance >= amount)
        {
            return true;
        }

        return false;
    }

    withdraw(amount)
    {
        if(this.checkWithdrawal(amount))
        {
            this.balance -= amount;
            this.transactions.push("User withdrew " + amount);
            return amount;
        }

        return 0;
    }

    calculateInterest()
    {
        return this.balance * this.interestRate
    }

    printTransactions()
    {
        for(let i of this.transactions)
        {
            console.log(i)
        }

    }
}

let newAccount = new Account(100)

// simulate user input
console.log(newAccount.checkBalance());
console.log(newAccount.withdraw(50));
console.log(newAccount.checkBalance());
console.log(newAccount.withdraw(70));
console.log(newAccount.deposit(150));
console.log(newAccount.calculateInterest());
newAccount.printTransactions();
