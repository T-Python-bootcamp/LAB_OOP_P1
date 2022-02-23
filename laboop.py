class AcountBank:
    def __init__(self, AccountNumber, owner, balance):
        self.AccountNumber = AccountNumber
        self.owner = owner
        self.balance = balance

    def Deposit(self, number):
        self.balance += number
        print(" Your balance is:", self.balance)

    def withdrawn(self, num):
        if self.balance > num:
            print("Your balance has been withdrawn", num)
        else:
            print("Your balance is less")

    def bankFees(self, num):
        self.balance = self.balance*93/100
        print(self.balance)

    def display(self, num):
        print("Your account information",
              self.AccountNumber, self.owner, self.balance)


obj = AcountBank(3456789, "Ahmed", 3000)
obj.Deposit(200)
obj.withdrawn(500)
obj.bankFees(522)
obj.display(5)
