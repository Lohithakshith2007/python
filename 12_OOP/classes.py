class Car:
    wheels=4
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year}) {self.wheels}")

car1=Car("TOYOTA","COROLLA",2024)
car2=Car("VW","VIRTUS",2024)

car1.display_info()
car2.display_info()