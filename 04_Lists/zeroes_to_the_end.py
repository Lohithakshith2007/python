numbers = [0, 5, 0, 3, 8, 0, 2, 0, 7]

zeroes_list=[]
non_zeroes_list=[]

for i in numbers:
    if i==0:
        zeroes_list.append(i)
    else:
        non_zeroes_list.append(i)

non_zeroes_list.extend(zeroes_list)
print(non_zeroes_list)