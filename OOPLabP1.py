
class Bank:
   

    def __init__(self,AccountNumber, owner, balance):
        self.AccountNumber=AccountNumber
        self.owner=owner
        self.balance=balance

    def Deposit(self,amount):
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def Withdrawal(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def bankFees(self):
         balanceFees = 0.07*self.balance
         return balanceFees

    def display(self):
        print("\n account information",self.AccountNumber,self.owner,self.balance)

obj = Bank(3456789, "Ahmad", 3000)

obj.Withdrawal(100)
obj.Deposit(200)
print(obj.bankFees())
obj.display()