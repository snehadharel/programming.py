#Syntax
#class classname:
#      prgram part:
# class A35:
#     x=10
#     y=20
#     name="abc"

# p1=A35
# #creating objects
# print("The value of x is",p1.x)
# print("The value of y is",p1.y)
# print("My name is",p1.name)

#WAP to print personal details using "class syntax".
# class PersonalDetails:
#     name="sneha"
#     age=19
#     gender="Female"
#     gmail="sneha@gmail.com"
#     number="123456789"
    
# p1=PersonalDetails
# print("My name is:", p1.name)
# print("My age is:", p1.age)
# print("Gender is:", p1.gender)
# print(" Email is :", p1.gmail)
# print("Phone  is :", p1.number)

#Create a class named Person using init function to assign the values for name and age,gender, and gmail.
class person:
    def __init__(self,name,age,gender,gmail):
        self.name=name
        self.age=age
        self.gender=gender
        self.gmail=gmail
p1=person("Sneha",19,"Female","sneha@gmail.com")

print("My name is ",p1.name,".")
print("My age is",p1.age,"years old.")
print("gender",p1.gender,".")
print("My gmail is",p1.gmail,".")

# class car: #declaring class
#     def __init__(self,model,make,year,cc):
#         self.model=model
#         self.make=make
#         self.year=year
#         self.cc=cc

# p1=car(" Toyota"," Corolla",2023,1500) #declaring objects for the above class.

# print("The model of the car is ",p1.model,".")
# print("The manufaturer of the car is",p1.make,".")
# print("The car has launched on",p1.year,".")
# print("The engine of the car is",p1.cc,".")

class car: 
    def __init__(self,model,make,year,cc):
        self.model=model
        self.make=make
        self.year=year
        self.cc=cc
    def myfunc(self):
        print("The model of the car is ",p1.model,".")
        print("The manufaturer of the car is",p1.make,".")
        print("The car has launched on",p1.year,".")
        print("The engine of the car is",p1.cc,".")

p1 = car(" Toyota"," Corolla",2023,1500)
p1.myfunc()
