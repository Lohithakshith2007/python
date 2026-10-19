try:
    file_name=input("enter the file name: ")
    with open(f"{file_name}.txt",'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("file not found")
else:
    print("file read successfully")
finally:
    print("task complete! ")