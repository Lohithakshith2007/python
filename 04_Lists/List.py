list1=[1,2,2,3,4,2,5,6]

list2=list.copy(list1) 
print("Copy of the list:", list2) # creates a copy of the list

sorted_list=sorted(list1) 
print("Sorted list:", sorted_list) # created a sorted copy of the lists

list1.append(7) 
print("After appending 7:", list1) # adds a new item to the list

list1.insert(1,99) 
print("After inserting 99 at index 1:", list1) # inserts at a particular index

list1.remove(99) 
print("After removing 99:", list1) # removes a particular element

last_element=list1.pop() # returns the last element
print("Last element removed:", last_element)

index_of_3=list1.index(3) # returns the index of the element
print("Index of 3:", index_of_3)

count_of_2=list1.count(2) # returns the number of occurrences of an element
print("Count of 2:", count_of_2)


# looping through the list
for item in list1:
    print(item)

for i,element in enumerate(list1):
    print(f"Index: {i}, Element: {element}")