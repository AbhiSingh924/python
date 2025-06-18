n = int(input("Enter the number for which you to calcuate its factorial:-"))
prod = 1

for i in range(n, 0, -1):
    # prod = prod*(i)
    prod *= i
    
print(f"Factorial of {n} is :- {prod}")