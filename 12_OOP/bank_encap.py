class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid")

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            print("invalid")

    def get_balance(self):
        return self.__balance

a1=Account("lohith",2000)
a1.deposit(500)
a1.withdraw(1000)
print(a1.get_balance())
