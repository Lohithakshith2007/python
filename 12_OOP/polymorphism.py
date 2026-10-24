class PaymentMethod:
    def pay(self,amount):
        print("processing payment")

class UPI(PaymentMethod):
    def pay(self,amount):
        print(f"paying ₹{amount}/- through upi")

class Card(PaymentMethod):
    def pay(self,amount):
        print(f"paying ₹{amount}/- through card")

class WalletPayment:
    def pay(self,amount):
            print(f"paying ₹{amount}/- through wallet")
    

payments=[PaymentMethod(),UPI(),Card(),WalletPayment()]

for p in payments:
    p.pay(3500)
