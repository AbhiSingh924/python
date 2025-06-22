str = input("Enter a string as an input:- ")
strNew = ""


# /****** SING BUILD IN FUNCTION "replace" ******/
# str = str.replace(" ","_") 

# /****** WITHOUT USING BUILD IN FUNCTION ******/
for ch in str:
    if ch == " ":
        strNew += '_'
    else:
        strNew += ch

print("String after replacing space(' ') with hyphen('_'):- ",strNew)