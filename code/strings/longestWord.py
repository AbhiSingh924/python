sentence = input("Enter a sentence: ")

longest_words = []
word = ""
for ch in sentence:
    if ch != " ":
        word += ch
    else:
        if word != "":
            longest_words.append(word)
            word = ""
if word != "":
    longest_words.append(word)

longest = ""
for w in longest_words:
    if len(w) > len(longest):
        longest = w

if longest != "":
    print("The longest word is:", longest)
else:
    print("No words found in the sentence.")