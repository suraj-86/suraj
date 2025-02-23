#create account class with 2 attributes - balance and account no.
#create method for debit and credit and printing balance


class Account:

    def __init__(self,bal,account_no):
        self.bal=bal
        self.acc=account_no

    def debit(self,debit):
        self.bal-=debit
        print("HI ",self.acc,"your account is debited for ",debit)
    
    def credit(self,credit):
        self.bal+=credit
        print("HI ",self.acc,"your account is credited for ",credit)
    

    def balance(self):
        print("HI ",self.acc,"your balance is ",self.bal)

a1=Account(10000,8676895110)
a1.balance()
a1.debit(100)
a1.credit(300)
a1.balance()