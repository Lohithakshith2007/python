input_list=[]

frequency_dict={}

count_of_mf=0
mf=None

count=int(input("how man numbers do u wnat to enter?: "))

# adding items ot frequenct_dict
for i in range(1,count+1):

    num=int(input(f'enter number {i}: '))
    input_list.append(num)

    if num not in frequency_dict:
        frequency_dict[num]=1
    else:
        frequency_dict[num]+=1

print(f'the final list is: {input_list}')
print('the final frequency is: ')

# determining the frequency and most frequent
for key,val in frequency_dict.items():
    print(f'the count of {key} is {val}')

    if val>count_of_mf:
        count_of_mf=val
        mf=key

print(frequency_dict)
print(f'the most frequent number is {mf} and it repeated {count_of_mf} times')

