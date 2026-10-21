class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

    def speak(self):
        print("wooff!!")

dog = Dog("Bruno", "Labrador")
print(dog.name,dog.breed)
dog.speak()