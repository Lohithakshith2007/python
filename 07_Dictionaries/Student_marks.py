student = {
    "name": "Lohith",
    "maths": 85,
    "science": 90
}

print(student['name'])
student['maths']=95
student['english']=88
print('science' in student)

for key,val in student.items():
    if key == 'name':
        continue
    print(key,val)

print(student.get('social',0))
print(student)