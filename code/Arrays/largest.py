n = int(input("Enter the total number of elements in a an array:- "))
arr = []

for i in range(n):
    element = int(input(f"Enter {i+1} element:- "))
    arr.append(element)
    
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print(f"Largest element in the given array is:- {largest}")