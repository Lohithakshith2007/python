nums_list=[]

count=int(input("How many numbers do you want to enter?: "))

sum=0
largest=None
smallest=None
even_nums=0
odd_nums=0
positive_nums=0
negative_nums=0
zeroes=0

for i in range(1,count+1):
    num=int(input(f"enter number {i}: "))
    
    if num==-999:
        print("stopping iteration")
        break

    nums_list.append(num)

    if num==0:
        zeroes+=1
        print("skipping the iteration")
        continue

    if largest is None or num>largest:
        largest=num

    if smallest is None or num<smallest:
        smallest=num

    if num%2==0:
        even_nums+=1
    else:
        odd_nums+=1

    if num>0:
        positive_nums+=1

    if num<0:
        negative_nums+=1

for i in nums_list:
    sum+=i

if len(nums_list)>0:
    average=sum/len(nums_list)
    print('the final list is: ',nums_list)
    print('the sum of the numbers is: ',sum)
    print('the average of the numbers is: ',average)
    print('the largest number is: ',largest)
    print('the smallest number is: ',smallest)
    print('the number of even numbers is: ',even_nums)
    print('the number of odd numbers is: ',odd_nums)
    print('the number of positive numbers is: ',positive_nums)
    print('the number of negative numbers is: ',negative_nums)
    print('the number of zeroes is: ',zeroes)
else:
    print("no numbers entered")
