def calculate_stats(nums):
    return min(nums),max(nums),sum(nums)

def normalize_price(price,discount):
    return price*(1-discount/100)

def add_tax(price):
    price=price*1.18
    return price


print(calculate_stats([1,2,3,4,5,6])) # returns a tuple of stats
print(add_tax(normalize_price(5000,10))) # returns price after 10% discount adn 18% tax 
    