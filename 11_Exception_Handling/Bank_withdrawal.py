class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    elif amount<=0:
        raise ValueError("withdrawal amount can't be zero or negative")
    return balance - amount


try:
    remaining = withdraw(300, -10)

except InsufficientBalanceError as error:
    print(error)
except ValueError as error:
    print(error)
else:
    print(remaining)
