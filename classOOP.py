class Bank:
   print("hi bank")
   def __init__(self,AccountNumber, owner, balance):
    self.AccountNumber= AccountNumber
    self.owner= owner
    self.balance = balance

   def Deposit(self,add ):
        self.balance += add 
        print("Deposit :{}".format(add))
 


   

   def Withdrawal(self,aa ):
        if self.balance > aa :
            self.balance -= aa 
            print("Withdrawal :{}".format(aa))



    


   def bankFees(self):
        self.balance=self.balance*93/100
        print("{}".format(self.balance))
    


   def display(self):
        print("Account Number  {}/  owner {}/ balance  {}/".format(self.AccountNumber,self.owner, self.balance))
 

   

user1=Bank(3456789,"Ahmed",3000)
user1.Deposit(200)
user1.Withdrawal(100)
user1.bankFees()
user1.display()