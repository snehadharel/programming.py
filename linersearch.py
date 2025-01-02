#linear search
def search(list, n, a):
    for i in range(0, n):
        if list[i] == a:
            return i
    return -1
    
list = [1, 2, 3, 4, 5, 6]
a = 4

n = len(list)
result = search(list, n, a)
if result == -1:
    print('No element found')

else:
    print('Element found at index', result)


# ANOTHER PROCESS

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

list = [2,3,10,20]
target = 1
result = linear_search(list,target)
if result != -1:
    print(f"linear search: element found at index {result}")
else:
    print(f"linear search: element not found")