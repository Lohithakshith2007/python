# Phase 8: Python Comprehensions

# 1. List Comprehension — Transform and Filter
numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]

cubes = [x**3 for x in numbers if x > 0 and x % 2 != 0]

print("Cubes of positive odd numbers:", cubes)


# 2. Dictionary Comprehension — Filter and Map
names = ["Mia", "Arun", "John", "Li", "Priya"]

names2 = {name: len(name) for name in names if len(name) >= 4}

print("Names and their lengths:", names2)


# 3. Set Comprehension — Unique Remainders
numbers = [3, 4, 5, 6, 7, 8, 9, 10]

rem = {n % 3 for n in numbers}

print("Unique remainders:", rem)


# 4. Nested List Comprehension — Flatten a List
groups = [[10, 20], [30, 40, 50], [60]]

flat = [num for row in groups for num in row]

print("Flattened list:", flat)