students = (
    ("Alex", 21, 85),
    ("Priya", 20, 86),
    ("Rahul", 22, 78),
    ("Sara", 21, 82),
    ("John", 20, 67)
)

highest=None
youngest=None
youngest_name=()
highest_marks=()
above_avg=()
total=0

for i in students:
    name,age,marks=i

    # determining all the students
    print(f"""name: {name}
    age: {age}
    marks: {marks}
    """)

    # determining students with highest marks
    if highest is None or marks>highest:
        highest=marks
        highest_marks=(name,)
    elif marks == highest:
        highest_marks += (name,)

    # determining the youngest student
    if youngest is None or age<youngest:
        youngest=age
        youngest_name+=(name,)

    # calculating total marks of the class
    total+=marks

# printing all students and students with highest marks 
print(f"the highest marks are: {highest}")
for i in highest_marks:
    print(i)

# printing the class average 
avg=total/len(students)
print(f"the class average is {avg}")

# students above class average 
for i in students:
    name,age,marks=i
    if marks>avg:
        above_avg+=(name,)

print("above avg are:")
for i in above_avg:
    print(i)

# printing the youngest student
print(f"the youngest student is {youngest_name}. age: {youngest}")
