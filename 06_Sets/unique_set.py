numbers = [4, 7, 2, 7, 9, 4, 1, 9, 5, 2, 8]
unique_set=set()
duplicate_set=set()

for i in numbers:
    if i not in unique_set:
        unique_set.add(i)
    else:
        duplicate_set.add(i)

print(numbers)
print(unique_set)
print(len(unique_set))

print(duplicate_set)

if 6 in unique_set:
    print("6 exists")

if  7 in duplicate_set:
    print("7 exists")