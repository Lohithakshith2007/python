numbers = [1,3,4, 5, 6]

for i in range(1,len(numbers)+1):
    if i not in numbers:
        print(i)
        break
