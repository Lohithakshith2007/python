numbers = [2, 4, 2, 7, 4, 2, 9, 7, 4]
freq={}

# method 1
for i in numbers:
    freq[i]=freq.get(i,0)+1

# method 2 
for i in numbers:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

print(freq)
