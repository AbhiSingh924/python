n = int(input("Enter the size of an array:- "))
arr = []

for i in range(n):
    num = int(input(f"Enter {i+1} element:- "))
    arr.append(num)
    
arrEven = []
arrodd = []

for i in range(n):
    if arr[i] % 2 == 0:
        arrEven.append(arr[i])
        
    else:
        arrodd.append(arr[i])
        
print("Even List:- ",arrEven)
print("Odd List:- ",arrodd)