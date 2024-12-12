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


#multilevel inheritance
class Person:
    def __init__(self, name):
        self.name = name
        

    def fun1(self):
        return f"Name: {self.name}"
          
class Man(Person):
    def __init__(self, name, age, gender):
        super().__init__(name)
        self.age = age
        self.gender = gender

    def fun2(self):
        info = super().fun1()
        return f"{info} \nAge: {self.age} \nGender: {self.gender}"
    
class He(Man):
    def __init__(self, name, age, gender, height):
        super().__init__(name, age, gender)
        self.height = height

    def fun3(self):
        info = super().fun2()
        return f"{info} \nHeight: {self.height}cm"
    
naam = He('John', 21, 'Male', 180)
print(naam.fun3())


#multiple inheritance
class Father:
    def display_father(self):
        print("John's Father")

class Mother:
    def display_mother(self):
        print("John's Mother")

class John(Father, Mother):
    def display_john(self):
        print("This is John")

# Create an object of the John class
j = John()
j.display_father()
j.display_mother()
j.display_john()




    