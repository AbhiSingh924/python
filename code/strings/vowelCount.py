str = input("Enter the string :")

def vowel_count(str):
    vowel  = "aeiouAEIOU"
    COUNT = 0
    
    for i in str:
        if i in vowel:
            COUNT += 1
    return COUNT

print("Number of vowels in the string is:", vowel_count(str))