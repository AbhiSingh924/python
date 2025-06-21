str1 = input("Enter the first string :-")
str2 = input("Enter the second string :-")

str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")

uncommonChar = ""

for ch in str1:
    if ch not in str2 and ch not in uncommonChar:
        uncommonChar += ch + " "

for ch in str2:
    if ch not in str1 and ch not in uncommonChar:
        uncommonChar += ch + " "
                
print("All Uncommon character from both the strings are as follow:- ")
print(uncommonChar)