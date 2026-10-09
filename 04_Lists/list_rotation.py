l=[1,2,3,4,5]
k=6

last_k=l[-k:]
last_k.extend(l[:-k])

if k<len(l):
    print(last_k)
else:
    print("exceeded length")