#file handling 
#READ/ WRITE(APPEND)

#File opening modes
# r-read
# w-write
# a-append(write)
# x-create
# b-binary
# t-text

# READING through File
# f=open("softwarica.txt","r")
# print(f.read())
# print(f.readline())#we use this readline() to read the first line of the file 
# print(f.readline())#so to read the second line we can use this same

# print(f.readline(2))#we can use this to print the certain letters og the name 

#loop to print the name stored in the files 
# for x in f:
#     print(x,end="")#end is used to remove the space between the line 

# print(f.readlines())#readlines will display the name in vertical linesss

f=open("C:\\Users\Dell\Desktop\programming.py\softwarica.txt","r")
print(f.readline())