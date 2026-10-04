marks=int(input("enter your marks: "))
attendance=int(input("enter your attendance percentage: "))

grade=None
result=None
reason=None

if marks in range(0,101) and attendance in range(0,101):
    print("-----result sheet-----")

    # deciding the grade
    if marks in range(90,101):
        grade='A'
    elif marks in range(75,90):
        grade='B'
    elif marks in range(60,75):
        grade='C'
    elif marks in range(40,60):
        grade='D'
    else:
        grade="F"

    # deciding the result
    if attendance<75 and marks<40:
        result="fail"
        reason="your marks and attendance are low"
    elif marks<40:
        result="fail"
        reason="your marks are low"
    elif attendance<75:
        result="fail"
        reason="your attendance is low"
    else:
        result="pass"

    # printing the result 
    if grade:
        print("Grade:",grade)
    if result:
        print("Result:",result)
    if reason:
        print("Reason:",reason)
    
else:
    print("enter a valid value")
