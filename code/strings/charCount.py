str = input("Enter a string containing both upper and lower case:- ")
upper_count = 0
lower_count = 0

for i in range(len(str)):
    if str[i] >= 'a' and str[i] <= 'z':
        lower_count += 1
        
    elif str[i] >= 'A' and str[i] <= 'Z':
        upper_count += 1
        
    else:
        continue
    
print("Upper Case Count in given String:- ",upper_count)
print("Lower Case Count in given String:- ",lower_count)