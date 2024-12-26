# #Stack

# stack=[]
# #push the data(insert)
# stack.append('Sneha')
# stack.append('Bini')
# stack.append('Sara')
# print("list data",stack)

# # delete items from the top in stack(pop)
# element=stack.pop()
# print("pop: ",element)
# print("list after pop",stack)

# # OR another process
# # stack.pop()
# # print(stack)

# #peek(selecting the items in lists)
# topelement=stack[-1]
# print("peek or selected item: ", topelement)

# # size or length
# print(len(stack))


stack = []
# Push foods into the stack
stack.append('momo')
stack.append('chowmein')
stack.append('pizza')
print("Stack after pushing foods:", stack)

# Pop an element from the stack
element = stack.pop()
print("Popped element:", element)
print("Stack after pop:", stack)

# Peek at the top element
top_element = stack[-1]
print("Top element:", top_element)

# Size of the stack
print("Stack size:", len(stack))

#To check whether stack is empty or not 
# print(not bool(stack))
isempty=not bool(stack)
print("Is stack empty: ", isempty)
