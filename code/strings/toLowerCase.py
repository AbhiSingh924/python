str = input("Enter the String : ")

def toLowerCase(str):
    result =""
    
    for i in range(len(str)):
        char = str[i]
        
        if 'A' <= char < 'Z':
            lower_case = chr(ord(char) + 32)
            result += lower_case
            
        else:
            result += char
            
    return result
    

print(toLowerCase(str))