num = int(input("Enter a number of your choice: - "))
rev = ""
temp = num 

while num > 0:
    rem = num % 10
    rev += str(rem) + ""
    num = num // 10

if temp == int(rev):
    print(f"{temp} is a Pallindromic number.")
    
else:
    print(f"{temp} is not a Pallindromic number.")
    
    