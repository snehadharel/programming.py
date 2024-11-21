#WAP to print addition, subtraction, multiply, floor division,division, and modulo.
a=33
b=5
def add():
    sum=a+b
    print("The sum of any two number is:", sum)
add()

a=33
b=5
def sub():
    sub=a-b
    print("The subtraction of any two number is:", sub)
sub()

a=5
b=5
def multiply():
    multiply=a*b
    print("The multiplication of any two number is:", multiply)
multiply()

a=25
b=5
def div():
    div=a/b
    print("The division of any two number is:", div)
div()

a=33.5
b=5
def floor():
    f=a//b
    f=int(f)
    print("The floor division of any two number is:", f)
floor()

a=33
b=5
def modulo():
    modulo=a%b
    print("The modulp of any two number is:", modulo)
modulo()

#WAP to print country name using function.
def cname(country="Nepal"):
    print("I am from " + " " +country)
cname("USA")
cname("India")
cname()
cname("Australia")
cname()

#WAP to display the following usig function in pyhton
# *
# **
# ***
# ****
# *****
# ******

def pattern(rows):
    for i in range(1, rows + 1):
        print(' * ' * i)

pattern(6)

#N
#NE
#NEP
#NEPA
#NEPAL

def display_pattern(word):
    for i in range(1, len(word) + 1):
        print(word[:i])


word = "NEPAL"
display_pattern(word)