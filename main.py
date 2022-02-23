class Bank() :

    def __init__(self, accountNumber, owner, balance ):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance
    
    def deposit(self, added):
        self.balance += added
        
    def withdrawal(self, withdrawed):
        if self.balance > withdrawed:
            self.balance -= withdrawed
            print("new balance is: {}".format(self.balance))
        else:
            print("Account balance is less than your withdrawel")
            
    def bankFees(self):
        self.balance = self.balance * 0.93
        print("this is the balance after bank fees are cut off: {}".format(self.balance))
        
    def display(self):
        print("Account number is: {}".format(self.accountNumber))
        print("Owner's name is: {}".format(self.owner))
        print("Acount balance is: {}".format(self.balance))
        
ahmedAcc = Bank(3456789, "Ahmed", 3000)

Bank.display(ahmedAcc)
Bank.withdrawal(ahmedAcc, 100)
Bank.deposit(ahmedAcc, 200)
Bank.bankFees(ahmedAcc)
Bank.display(ahmedAcc)
