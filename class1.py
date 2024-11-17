# name=input("enter your name:")
# print("your name is ", name)

print('Hello I am a discplined student of "Sofrwarica"')

print("It's too cold today" )

#This is a single-line comment.
"""
This is a multi-line comment.
Hello World!!
"""

# Different variable types
name = "sneha"        # String
age = 19             # Integer
height = 5.3         # Float
is_active = True      # Boolean
print(name)           
print(age)           
print(height)        
print(is_active)      

# Given variables
A = 10
B = 20.40
C = "hello"

# Check the types
print(type(A)) 
print(type(B)) 
print(type(C))  

#to print both single(')and double("")quote we have used (''')
print('''Hello! Welcome to "Python". It's so awesome''')

#WAP to print maximum between two numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("The maximum number is:", a)
else:
    print("The maximum number is:", b)

#WAP to print minimum among three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Using conditional statements to find the minimum
if a <= b and a <= c:
    print("The minimum number is:", a)
elif b <= a and b <= c:
    print("The minimum number is:", b)
else:
    print("The minimum number is:",c)

#WAP to print even numbers from 1 to 100.
print([i for i in range(1, 101) if i % 2 ==0])

#WAP tp print your name 10 times.
name = "SNEHA"
print((name + "\n") * 10)

#WAP to print odd numbers from 100 to 50.
print(list(range(99, 49, -2)))

#WAP to print prepare your result sheet.

name = str(input("Enter your name: "))
roll_no = int(input("Enter your roll no: "))
marks = int(input("Enter your marks: "))
print('Name: ', name)
print('Roll No: ', roll_no)
if marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

elif marks >= 50:
    print("Grade: E")

else:
    print("Grade: Fail")