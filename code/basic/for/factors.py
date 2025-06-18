num = int(input("Enter the number:- "))
factors = ""

for i in range(1, num+1):
    if num % i == 0:
        factors += str(i) + " "
    
print(f"All the Factors of {num} are:- {factors} ")