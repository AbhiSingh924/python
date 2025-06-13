str = input("Enter the String that you want to check for palindrome :")

def is_palindrome(str):
    
    str = str.lower()
    str = str.replace(" ","")
    
    for i in range(len(str)//2):
        if str[i] != str[-(i+1)]:
            print("The string is not a palindrome")
            break
        else: 
            print("The string is a palindrome")
            break
            
is_palindrome(str)