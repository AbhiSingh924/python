n = int(input("Enter the size of an array:- "))
arr = []

for i in range(n):
    num = int(input(f"Enetr {i+1} element:- "))
    arr.append(num)

for i in range(0, n):
    min = i   
    for j in range(i+1, n-1):
        if arr[j] < arr[min]:
            arr[j], arr[min] = arr[min], arr[j]
        
print("Sorted array is:- ",arr)