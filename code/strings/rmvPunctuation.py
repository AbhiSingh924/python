str = input("Provide a string as an input:- ")

strNew = ""

for ch in str:
    if not((ch == ',') or (ch == '?') or (ch == '.')):
        strNew += ch
        
print("New string after removing Punctuations:- ",strNew)
