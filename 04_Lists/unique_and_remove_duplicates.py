numbers = [1,5,2,4,2,6,9,5,1,7,6]
unique_list=[]

duplicates=[]

largest=None
second_largest=None

for i in numbers:
    if i not in unique_list:
        unique_list.append(i)

    if numbers.count(i)>1 and i not in duplicates:
        duplicates.append(i)

for i in unique_list:
        if largest is None or i>largest:
            second_largest=largest
            largest=i
        elif second_largest is None or i>second_largest:
             second_largest=i

print(f"original list: {numbers}")
print(f"unique list: {sorted(unique_list)}")
print(f"duplicates: {sorted(duplicates)}")

print(f"largest: {largest}")
print(f"second largest: {second_largest}")
