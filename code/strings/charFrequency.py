str = input("Enter the string : ")
str = str.lower()
def char_frequency(str):
    frequency = {}
    for i in range (len(str)):
        char = str[i]
        found = False
        
        for key in frequency:
            if key == char:
                frequency[key] +=1
                found = True
                break
            
        if not found:
            frequency[char] = 1 
        
    return frequency

print(char_frequency(str))
        
