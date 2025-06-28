n = int(input("Enter the size of array:- "))

arr = []

for i in range(n):
    num = int(input(f"Enter the {i+1} element:- "))
    arr.append(num)
    
sec_large = 0
large = arr[0]
for i in range(1, n):
    if arr[i] > large:
        large = arr[i]
        sec_large = arr[i - 1]
        
print(f"Second Largest Element is:- {sec_large}")
