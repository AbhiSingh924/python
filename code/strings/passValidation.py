pass_str = input("Please Enter a password of your choice that contain both upeer case & lower case alphabets, Number and special char:-  ")

countLower = 0 
countUpper = 0 
CountDigit = 0 
count = 0 

for ch in pass_str:
    if ('a' <= ch <= 'z'):
        countLower += 1
        
    elif ('A' <= ch <= 'Z'):
        countUpper += 1
        
    elif ('0' <= ch <= '9'):
        CountDigit += 1
        
    else:
        count += 1
        

if len(pass_str) < 8 or CountDigit == 0 or countUpper == 0 or count == 0 or countLower == 0:
    print("WEAK Password 😞 Please recheck your password")
    if len(pass_str) < 8:
        print("- Password must be at least 8 characters long.")
    if countLower == 0:
        print("- Password must contain at least one lowercase letter.")
    if countUpper == 0:
        print("- Password must contain at least one uppercase letter.")
    if CountDigit == 0:
        print("- Password must contain at least one digit.")
    if count == 0:
        print("- Password must contain at least one special character.")

else: 
    print("Strong Password 😊")