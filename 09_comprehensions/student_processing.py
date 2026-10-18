scores = {
    "Arun": 82,
    "Mia": 45,
    "John": 97,
    "Priya": 67,
    "Sam": 38,
    "Liam": 76
}

# creating the list pf passed students
passed={name:marks for name,marks in scores.items() if marks>=60}
print(f"passed stdents are: {passed}")

# creating the list of failed student names
failed=[name for name,marks in scores.items() if marks<60]
print(f"failed students are: {failed}")

# dictionary of students after adding 5 bonus marks
bonus_scores={name:min(score+5,100) for name,score in scores.items()}
print(bonus_scores)