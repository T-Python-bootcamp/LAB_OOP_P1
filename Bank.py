class Bank:
    def __init__(self, accountNumber, owner, balance):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance

    def Deposit(self, num):
        self.newBalance = self.balance + num
        print(f'deposit successfull, new balance is {self.newBalance}')

    def Withdrawal(self, num):
        if self.balance > num:
            self.newBalance = self.balance - num
            print(f"withdraw is successfull, new balance is {self.newBalance}")
        else:
            print("insuffucient balance")

    def bankFees(self, fees):
        bFees = self.balance * fees
        print(f"bank fees are {bFees}")
    
    def display(self):
        print(self.accountNumber)
        print(self.owner)
        print(self.newBalance)
    

account = Bank(3456789, "Ahmed", 3000)

print(account.Withdrawal(100))
print("_______________")
print(account.Deposit(200))
print("_______________")
print(account.bankFees(0.07))
print("_______________")
print(account.display())
