str = input("Enter the string containg alphabet, interger, special character :- ")

str = str.replace(" ","")

count = 0

for ch in str:
    if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
        count += 1
        
print("Total number of special character in a string is :-  ",count)