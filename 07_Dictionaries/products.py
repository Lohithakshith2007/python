products = {
    "laptop": 50000,
    "mouse": 800,
    "keyboard": 1500,
    "monitor": 12000
}

print(f"the products are \n {products.keys()}")
print(f"the prices are \n {products.values()}")
products['headphones']=2000
products['mouse']=1000
products.pop('keyboard')
print(products.get('laptop',0))
print(products)

for key,val in products.items():
    if val>5000:
        print(key,val)