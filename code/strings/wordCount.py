sentence = input("Enter a sentence: ")

count = 0

if len(sentence) > 0:
    count +=1
else:
    print("No words found in the sentence.")

for ch in sentence:
    if ch == " ":
        count += 1

print("Total number of words in this sentence is :", count)