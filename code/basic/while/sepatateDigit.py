num = int(input("Enter a number of your choice:- "))
digit = ""

while num > 0:
    rem = num % 10
    digit += str(rem) + " "
    num = num // 10

digit = "".join(reversed(digit))
print(digit) 