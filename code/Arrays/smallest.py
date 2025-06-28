n = int(input("Enter the size of array:- "))
arr = []

for i in range(n):
    element = int(input(f"Enter the {i+1} element of the array:- "))
    arr.append(element)
    
smallest = arr[0]
for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]
        
print(f"Smallent element in the given array is:- {smallest}")
