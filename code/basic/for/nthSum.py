n = int(input("Till where do you want the sum of Enter that number:- "))

sum = 0

for i in range(n, 0, -1):
    sum = sum + i
    
print("Sum upto nth term is equal to ",sum)