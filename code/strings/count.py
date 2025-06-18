str = input("Enter a string that contains Chars, Digits, Symbols etc:- ")
Chars = 0
Digits = 0
Symbols = 0
str = str.replace(" ","")

for i in range (len(str)):
    ch = str[i]
    
    if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
        Chars += 1
    
    elif ch >= '0' and ch <= '9':
        Digits += 1
    
    else:
        Symbols += 1
        
print(f"Chars = {Chars}")
print(f"Digits = {Digits}")
print(f"Symbols = {Symbols}")