str = input("Enter a string: ")

def to_uppercase(str):
    
    result = ""
    
    for i in range(len(str)):
        ch = str[i]
        
        if 'a' <= ch <= 'z':
            upper_ch = chr(ord(ch) - 32)
            result += upper_ch
            
        else:
            result += ch
            
    return result

print(to_uppercase(str))