str = input("Enter the input String:- ")
strNew = ""

for ch in str:
    if('a' <= ch <= 'z'):
        ch = chr(ord(ch) - 32)
        strNew += ch
    elif('A' <= ch <= 'Z'):
        ch = chr(ord(ch) + 32)
        strNew += ch
    else:   
        strNew += ch
    
print(strNew)