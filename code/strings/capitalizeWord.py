str = input("Enter the string : ")

def upper_case(ch):
        if 'a' <= ch <= 'z':
            return chr(ord(ch)-32)

result = ""

if 'a' <= str[0] <= 'z':
    result+= upper_case(str[0])
else:
    result += str[0]

i = 1 
while i < (len(str)):
    if str[i-1] == " " and 'a'<= str[i] <= 'z':
        upperCase1st = upper_case(str[i])
        result += upperCase1st
    else:
        result += str[i]
    i += 1

print("String after capitalizing 1st letter of each word : ",result)        
    