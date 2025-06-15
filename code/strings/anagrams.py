str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

s1 = ""
for ch in str1:
    if ch != " ":
        if 'A' <= ch <= 'Z':
            s1 += chr(ord(ch) + 32)
        else:
            s1 += ch

s2 = ""
for ch in str2:
    if ch != " ":
        if 'A' <= ch <= 'Z':
            s2 += chr(ord(ch) + 32)
        else:
            s2 += ch

def count_chars(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count

count1 = count_chars(s1)
count2 = count_chars(s2)

is_anagram = True
if len(count1) != len(count2):
    is_anagram = False
else:
    for key in count1:
        if key not in count2 or count1[key] != count2[key]:
            is_anagram = False
            break

if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")