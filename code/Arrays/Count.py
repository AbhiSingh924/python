n = int(input("Enter the size of an array:- "))
arr = []

for i in range(n):
    num = int(input(f"Enter {i+1} element:- "))
    arr.append(num)
  
evenCount = 0
oddCount = 0  
for i in range(n):
    if arr[i] % 2 == 0:
        evenCount += 1
    
    else:
        oddCount += 1

print(f"Even Count = {evenCount} \n Odd Count = {oddCount}")
    