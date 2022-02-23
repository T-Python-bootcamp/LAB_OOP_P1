
class Bank(object):

    def __init__(self,AccountNumber, owner, balance):
        self.AccountNumber=AccountNumber
        self.owner=owner
        self.balance=balance

    def Deposit(self,amount):
        self.balance+=amount

    def Withdrawal(self,amount):
        if(self.balance<amount):
            return False
        else:
            self.balance-=amount
            return True

    def bankFees(self):
        fee=self.balance*0.07
        print("Bank fees:",fee)
        self.balance-=fee

    def display(self):
        print("\nAccount Number: {}\nOwner: {}".format(self.AccountNumber,self.owner))
        print(f"With balance of: {self.balance}\n")


user1 = Bank(3456789,'Ahmed',3000)
print(user1.Withdrawal(100))
user1.Deposit(200)
user1.bankFees()
user1.display()