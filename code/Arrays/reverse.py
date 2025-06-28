n = int(input("Enter the length of array:- "))
arr = []
rev = []

for i in range(n):
    element = int(input(f"Enter {i+1} element:- "))
    arr.append(element)
    
for i in range(n-1, -1, -1):
    rev.append(arr[i])
    
print("Actual array is:- ",arr)    
print("Reversed array is:- ",rev)
    