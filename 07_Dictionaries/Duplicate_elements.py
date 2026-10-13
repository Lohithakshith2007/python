numbers = [2, 4, 2, 7, 4, 2, 9, 7, 4]
freq={}

# method 1
for i in numbers:
    freq[i]=freq.get(i,0)+1

for key,val in freq.items():
    if freq[key]>1:
        print(f"{key} appears {val} times")