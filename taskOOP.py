
class BankAccount:

    

    def __init__(self, AccountNumber, owner, balance ) :
        self.AccountNumber = AccountNumber
        self.owner = owner
        self.balance = balance



    def Deposit(self, addAmount) :
        self.balance += addAmount 
        print("\n Hello, you can add amount Here : {}".format(addAmount)) 



    def Withdrawal(self, pull) :
        self.balance > pull
        print("\n Hello, you can pull from balance Here : {}".format(pull)) 




    def bankFees(self) : 
        self.balance = self.balance *93/100 
        print ( "\n You can take commission from here :{}".format (self.balance))

    
    def display(self) :
        self.balance 
        print ( "\n AccountNumber: {} \n owner:{} \n balance:{}".format(self.AccountNumber,self.owner,self.balance)) 


clint = BankAccount ( 3456789, "Ahmed", 3000 ) 

clint.Deposit(100)
clint.Withdrawal(200)
clint.bankFees()
clint.display()   

