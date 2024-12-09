# class ParentClass:
#     #parent class methods and attributes
#     pass

# class ChildClass(ParentClass):
#     #child class inherits from parentclass
#     pass

#SINGLE INHERITANCE 
#WAP to write single inheritance of students. 
class Student:
    def __init__(self, name):
        self.name = name

    def display_details(self):
        return f"{self.name}"

class sneha(Student):
    def student_details(self):
        return f"Sneha is {self.name}"

# Create an object of the classA class
s = sneha(" from ethical ")
print(s.student_details())

#for car 
class Car:
    def __init__(self, model):
        self.model = model

    def display_details(self):
        return f"{self.model} is a car available in 2024."

class Tesla(Car):
    def car_details(self):
        return f"Tesla is {self.model}"

# Create an object of the Tesla class
t = Tesla("Model S")
print(t.car_details())
print(t.display_details())


    