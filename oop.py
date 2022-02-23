class Bank:
    def __init__(self, AccountNumber, owner, balance):
        self.AccountNumber = AccountNumber
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawl(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Withdrawl amount is more than the balance"
    
    def bankFees(self):
        fees = round(self.balance * 0.07)
        self.balance -= self.balance * 0.07
        return fees
    
    def display(self):
        print(f"\nAccount info\nAccountNumber: {self.AccountNumber}\nOwner: {self.owner}\nBalance: {self.balance}")


account1 = Bank(3456789, "Ahmad", 3000)

bankFees = account1.bankFees()
account1.withdrawl(100)
account1.deposit(200)

print("Balance: ",account1.balance)
print("Bank fees: ",bankFees)
account1.display()