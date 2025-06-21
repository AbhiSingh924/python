str1 = input("Enter the first string:- ")
str2 = input("Enter the second string:- ")

newStr = ""

for ch in str1:
    if ch not in str2:
        newStr += ch
        
newStr += " " + str2 

print("New String after removing all the char of str1 that are also present in str2:- ",newStr)