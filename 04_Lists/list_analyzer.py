li=[]

largest=None
smallest=None
total=0
even_numbers=0
odd_numbers=0

number_of_items=int(input("how many numbers do you want to enter?: "))

for i in range(number_of_items):
    num=int(input(f"enter number {i}: "))
    li.append(num)
    total+=num

    if largest is None or num>largest:
        largest=num

    if smallest is None or num<smallest:
        smallest=num

    if num%2==0:
        even_numbers+=1
    else:
        odd_numbers+=1

print(f"""Analysis of the list:
- length: {len(li)}
- Largest number: {largest}
- Smallest number: {smallest}
- total of all numbers: {total}
- Number of even numbers: {even_numbers}
- Number of odd numbers: {odd_numbers}""")

print(f"sorted list: {sorted(li)}")
print(f"reversed list: {list(reversed(li))}")

searching_num=int(input("enter the number you want to search: "))

if searching_num in li:
    print(f"found at index {li.index(searching_num)}")
    print(f"occurrences: {li.count(searching_num)}")
else:
    print("number not found")