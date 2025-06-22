str = input("Enter a string as an input:- ")

count = 0

for ch in str:
    if not(( '0' <= ch <= '9') or (ch == " ")):
        count += 1
        
if count == 0:
    print("Entered string contains only Digit.")
else:
    print("Entered string contains not only Digits but also Other characters.")
