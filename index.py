
class Bank:
    def __init__(self,AccountNumber, owner, balance):
        self.AccountNumber=AccountNumber
        self.owner=owner
        self.balance=balance
    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f'{amount} riyals were deducted from your bank balance')
        else:
            print("Balance is not enough")
    def deposit(self,amount):
        self.balance+=amount
        print(f'{amount} riyals were deposited to your bank balance')
    def bankFees(self):
        newbalance=self.balance*93/100
        fees=self.balance-newbalance
        self.balance=fees
        print(f'the bank fees is {fees} riyals')
    def display(self):
        print(f'account number : {self.AccountNumber} \n owner : {self.owner} \n balance : {self.balance}')
account1=Bank(3456789,"Ahmed",3000)
account1.withdrawal(100)
account1.deposit(200)
account1.bankFees()
account1.display()