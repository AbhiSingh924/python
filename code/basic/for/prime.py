num = int(input("Enter a number to if it's prime or not:- "))

count = 0

if num == 1:
    print("1 is neither prime nor composit.")   

else:
    for i in range(1, (num // 2 + 1)):
        if num % i == 0:
            count +=1
        
    if count > 2:
        print(f"{num} is not a prime number.")
    
    else:
        print(f"{num} is a prime number.")