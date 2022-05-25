const docBankBalance = document.getElementById('bank_balance')
const docDeposit = document.getElementById('deposit')
const depositSubmit = document.getElementById('deposit-submit')
const docWithdraw = document.getElementById('withdraw')
const withdrawSubmit = document.getElementById('withdraw-submit')
const docTransactionHistory = document.getElementById('transaction_history')

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

        return -1;
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
// console.log(newAccount.checkBalance());
// console.log(newAccount.withdraw(50));
// console.log(newAccount.checkBalance());
// console.log(newAccount.withdraw(70));
// console.log(newAccount.deposit(150));
// console.log(newAccount.calculateInterest());
// newAccount.printTransactions();
docBankBalance.innerText = 'Your current balance is $' + newAccount.checkBalance()

depositSubmit.addEventListener('click', function(){
    newAccount.deposit(parseFloat(docDeposit.value));
    alert(`Deposited $${docDeposit.value}`)
    // event.preventDefault()
    docBankBalance.innerText = 'Your current balance is $' + newAccount.checkBalance()
    docTransactionHistory.innerText = newAccount.transactions
})

withdrawSubmit.addEventListener('click', function(){
    if(newAccount.withdraw(parseFloat(docWithdraw.value)) == -1){
        alert("Withdraw Failed, Insufficient Funds")
    }
    else{
        alert(`Withdrew $${docWithdraw.value}`)
    }
    docBankBalance.innerText = 'Your current balance is $' + newAccount.checkBalance()
    // event.preventDefault()
    docTransactionHistory.innerText = newAccount.transactions
})

docTransactionHistory.innerText = newAccount.transactions