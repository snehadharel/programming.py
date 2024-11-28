#perform multiple operations in tuple
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Basic operations
#inserting element 
my_tuple = my_tuple + (10,)
print(my_tuple) 

print("Tuple:", my_tuple) 
print("Indexing:", my_tuple[0])   
print("Slicing:", my_tuple[1:4])   
print("Concatenation:", my_tuple + (6, 7))  
print("Repetition:", my_tuple * 2)        
print("Length:", len(my_tuple))    
print("Min:", min(my_tuple))      
print("Max:", max(my_tuple))     
print("Count of 2:", my_tuple.count(2))  
print("Index of 3:", my_tuple.index(3))  
print("Membership:", 4 in my_tuple)     

# Looping through tuple
print("Elements:", [x for x in my_tuple])  

#to make single value of tuple we can give single comma , 
tuple1=("sneha",)
print(type(tuple1))
