str = input("Enter the string: ")

def removeVowel(s):
    
    vowel = "aeiouAEIOU"
    result = ""
    
    for i in range(len(s)):
        is_vowel = False
        for j in range(len(vowel)):
            if s[i] == vowel[j]:
                is_vowel = True
                break
            
        if not is_vowel:
            result += s[i]
            
    return result

print(removeVowel(str))