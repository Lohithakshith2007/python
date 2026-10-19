try:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
except ValueError:
    print("enter a valid integer")
else:
    print(x,y)
finally:
    print("calculation finished")