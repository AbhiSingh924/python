str = input("Enter the string : ")

def Consonant_count(str):
    vowel = "aeiouAEIOU"
    count = 0
    for i in str:
        if i not in vowel and i.isalpha():
            count += 1
    return count

print("Number of consonants in the string is:", Consonant_count(str))
