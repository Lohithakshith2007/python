def get_passed_students(students):
    passed=[]
    for name,mark in students.items():
        if mark>=40:
            passed.append(name)
    return passed
