class BankAccount:
    bank_name="SecureBank"

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def display_info(self):
        print(self.owner,self.balance)

    @classmethod
    def from_string(cls, data):
        owner,balance=data.split(",")
        return cls(owner,int(balance))

    @staticmethod
    def is_valid_amount(amount):
        return amount>0

account1 = BankAccount("Priya", 8000)
account2 = BankAccount.from_string("Ravi,5000")

account1.display_info()
account2.display_info()

print(BankAccount.is_valid_amount(500))   # True
print(BankAccount.is_valid_amount(-100))  # False
print(BankAccount.bank_name)              # SecureBank