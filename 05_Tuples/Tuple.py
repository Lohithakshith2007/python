# unpacking
student = ("Alex", 21, "Computer Science")

name,age,course=student
print(name,age,course)

# swapping numbers 
a=10
b=15
print("before swapping: ",a,b)
a,b=b,a
print(f"after swapping: {a,b}")

# finding middle elements 
numbers = (10, 20, 30, 40, 50, 60, 70)

first,*middle,last=numbers
print(middle)

# tuple ops 
data = (5, 10, 15, 10, 20, 10, 25)
total=0

print(data.count(10))
print(data.index(20))
data2=tuple(i for i in data if i>10)
print(data2)

for i in data:
    total+=i
print(total)