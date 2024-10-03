class Account():

    def __init__(self,name,bal,acno):

        self.bal=bal
        self.name=name
        self.acno=acno

        print("hello",self.name)

    def debit(self,amt):

        self.amt=amt
        self.bal= self.bal-amt
        print("Account Debited with Amount of:",self.amt)

    def credit(self,amt):
        self.amt=amt
        self.bal=self.bal+amt
        print("Accout Credited with Amount of:",self.amt)

    def balance(self):

        print(self.bal,"Is the total balance in your account")


p1=Account("Karan",5,20123)



p1.debit(5)

p1.credit(4)

p1.balance()

print(p1.name)