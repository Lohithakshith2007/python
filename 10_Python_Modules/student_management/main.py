from student import get_passed_students, calculate_average

s={
    "Arun": 75,
    "Priya": 32,
    "Rahul": 60,
    "Sneha": 25
}

if __name__=="__main__":
    print(calculate_average(s))
    print(get_passed_students(s))