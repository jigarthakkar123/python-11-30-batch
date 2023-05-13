class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With  ",self.balance," Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry Insufficient Fund")
    def checkBalance(self):
        print("Current Balance : ",self.balance)
b1=Bank()
b1.openAccount(101,"Jigar",1000)
b1.deposit(5000)
b1.checkBalance()
b1.withdraw(8000)
b1.checkBalance()
