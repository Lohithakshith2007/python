try:
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    result=a/b
except ValueError:
    print("enter a valid integer")
except ZeroDivisionError:
    print("cannot divide with zero")
else:
    print(f"division is {result}")
finally:
    print("Calculation finished")