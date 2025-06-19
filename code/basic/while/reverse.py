num = int(input("Enter the number that you want to reverse:- "))
rev = ""

while num > 0:
    rem = num % 10
    rev += str(rem) + ""
    num = num // 10

# rev = rev.replace(" ", "")
print(rev) 