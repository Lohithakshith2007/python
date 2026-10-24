class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amnt):
        if amnt<0:
            raise ValueError("asdfghjkl")

        self._balance=amnt

account = BankAccount("Arun", 1000)

print(account.balance)  # 1000

account.balance = 1500
print(account.balance)  # 1500

account.balance = -200  # Raises ValueError