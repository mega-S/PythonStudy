class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("User \"", self.name, "\" was deleted!!!")

    def displayInfo(self):
        print("Hello", self.name, "You are", self.age, "years old.")

class Animal:

    def __init__(self, animal, name, paws):
        self.animal = animal
        self.name = name
        self.paws = paws

    def displayInfo(self, someFact):
        print("This is a", self.animal, ". It`s name", self.name, ". And it has", self.paws, "paws.", "This is some fact:", someFact)
