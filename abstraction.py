from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method

    def common_behavior(self):
        print("All animals need food to survive.")  # Concrete method

# Concrete class
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Using the classes
dog = Dog()
dog.sound()  
dog.common_behavior()  

cat = Cat()
cat.sound() 
cat.common_behavior()

