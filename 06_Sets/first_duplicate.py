numbers = [4, 2, 7, 2, 4, 9, 7, 7, 1, 4]

seen=set()

for i in numbers:
    if i in seen:
        print(f"{i} is the first duplicate")
        break
    seen.add(i)