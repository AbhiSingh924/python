n = int(input("Enter the size of the array:- "))
arr = []
for i in range(n):
    num = int(input(f"Enter {i+1} element:- "))
    arr.append(num)
    
element = int(input("Enter the element to be searched:- "))
found = False
for i in range(n):
    if arr[i] == element:
        found = True
        
if found == True:
    print("Element Found.")

else:
    print("Element not Found.")  