str1 = input("Enter the First String :- ")
str2 = input("Enter the Second String :- ")

str1 = str1.replace(" ","")
str2 = str2.replace(" ","")

commonChar = ""

for i in range (len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            commonChar += str1[i] + " "
            
print("Common Character between both the string is :- ", commonChar)