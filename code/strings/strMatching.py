sentence = input("Enter the sentence:- ")
pattern = input("Enter the string that you want to search:- ")

found = False

for i in range(len(sentence) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if sentence[i + j] != pattern[j]:
            match = False
            break
        
    if match:
        found = True
        break
    
if found:
    print(f"Pattern {pattern} found in the string.")
else:
    print(f"Pattern {pattern} not found in the string.")