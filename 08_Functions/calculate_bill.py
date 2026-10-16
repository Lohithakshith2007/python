def calculate_bill(price,quantity=1,discount=0):
    total=price*quantity
    final_bill=total*(1-(discount/100))
    return final_bill

print(calculate_bill(100))              # 100
print(calculate_bill(100, 3))            # 300
print(calculate_bill(100, 3, 10))        # 270
print(calculate_bill(100, discount=20))  # 80