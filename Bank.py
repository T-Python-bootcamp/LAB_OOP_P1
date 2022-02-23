class Bank:
    def __init__(self, accountNumber, owner, balance):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance

    def Deposit(self, num):
        self.balance = self.balance + num
        print('deposit successfull, new balance is ,', self.balance)

    def Withdrawal(self, num):
        if self.balance > num:
            self.balance = self.balance - num
            print(f"withdraw is successfull, new balance is {self.balance}")
        else:
            print("insuffucient balance")

    def bankFees(self, fees):
        bFees = self.balance * fees
        print(f"bank fees are {bFees}")
    
    def display(self):
        print(self.accountNumber)
        print(self.owner)
        print(self.balance)
    

account = Bank(3456789, "Ahmed", 3000)

account.Withdrawal(100)
print("_______________")
account.Deposit(200)
print("_______________")
account.bankFees(0.07)
print("_______________")
account.display()
