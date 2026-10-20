class Employee:
    company="TechCorp"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_info(self):
        print(self.name,self.salary,self.company)

emp1 = Employee("Lohithakshith", 250000)
emp2 = Employee("Alex", 180000)

Employee.company = "NewTech"

emp1.display_info()
emp2.display_info()