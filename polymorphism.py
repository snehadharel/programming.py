class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print(f"Student Name: {self.name}, ID: {self.id}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")

class Admin:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        print(f"Admin Name: {self.name}, Role: {self.role}")

# Creating instances
student1 = Student("sneha", "S12345")
teacher1 = Teacher("Mr. Smith", "Mathematics")
admin1 = Admin("Mrs. Johnson", "Principal")

# Demonstrating polymorphism
for user in (student1, teacher1, admin1):
    user.display_info()
