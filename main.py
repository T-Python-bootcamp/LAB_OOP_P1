from re import S


class Bank:


    def __init__(self , balance , AcccountNumber , owner ):
        self.balance = balance
        self.AccountNumber = AcccountNumber
        self.owner = owner

    def Deposit(self , balance):
        self.balance += balance
        print(f"Deposit : {self.balance} riyals")
    
    def Withdrawal(self , balance):
        if balance <= self.balance:
            self.balance -= balance
            print(f"Withdraw:{self.balance} riyals")
        else : 
            print(f"Balance is insufficient \n Balance is {self.balance}")
        
    def bankFees(self):
        self.balance = self.balance * 0.07
        print(f"{self.balance} the bank Fees")

    def display(self):
        print("Display account information:")
        print(f"Account Number:{self.AccountNumber}")
        print(f"Owner:{self.owner}")
        print(f"Balance:{self.balance}")

c = Bank(300,345678,"Ahmed")
c.Deposit(50)
c.Withdrawal(100)
c.bankFees()
c.display()

