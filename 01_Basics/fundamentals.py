# 1. Variables

name = "Lohith"
age = 20

print(name)
print(age)


# 2. Dynamic Typing

x = 10
print(type(x))

x = "Hello"
print(type(x))


# 3. Data Types

integer = 10
floating = 3.14
string = "Python"
boolean = True
nothing = None

print(type(integer))
print(type(floating))
print(type(string))
print(type(boolean))
print(type(nothing))


# 4. Type Conversion

print(int("10"))
print(float("3.14"))
print(str(100))
print(bool(1))


# 5. type()

x = 10

print(type(x))


# 6. isinstance()

x = 10

print(isinstance(x, int))
print(isinstance(x, str))


# 7. Mutable vs Immutable

# Immutable
name = "Python"
# name[0] = "J"    # Error

# Mutable
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)


# 8. None

result = None

print(result)

if result is None:
    print("No value")