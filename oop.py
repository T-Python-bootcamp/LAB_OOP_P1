class Bank:
    def __init__(self,AccountNumber, owner, balance):
        self.AccountNumber = AccountNumber
        self.owner = owner
        self.balance = balance

    def Deposit(self,money ):
        self.balance += money 
        print("Deposit :{}".format(money))

    def Withdrawal(self,money ):
        if self.balance > money :
            self.balance -= money 
            print("Withdrawal :{}".format(money))

    def bankFees(self):
        self.balance*93/100
        print("Fees :{}".format(self.balance))

    def display(self):
        print("Account Number : {} , owner : {} , balance : {}  ...".format(self.AccountNumber,self.owner,self.balance))

################################

user1=Bank(3456789,"Ahmed",3000)
user1.Deposit(200)
user1.Withdrawal(100)
user1.bankFees()
user1.display() 