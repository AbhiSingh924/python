str = input("Enter a string as an input:- ")

count = 0

for ch in str:
    if not(('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or (ch == " ")):
        count += 1
        
if count == 0:
    print("Entered string contains only Alphabets.")
else:
    print("Entered string contains not only Alphabets but also Other characters.")
