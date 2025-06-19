# A number whose sum of Factors is equql to the number itself.
# Example:- 6 = 1, 2, 3
# 1 + 2 + 3 = 6

num = int(input("Enter a number:- "))
sum = 0

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        sum += i
        
if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    