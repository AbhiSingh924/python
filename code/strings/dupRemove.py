str = input("Enter a strint as input:- ")

strNew = ""

for ch in str:
    if ch not in strNew or ch == " ":
        strNew += ch
        
print("String after removing duplicate chaacter:- ")
print(strNew)