str = input("Enter the sentence:- ")

words = []
word = ""

for ch in str:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
            
if word != "":
    words.append(word)
    
rev_sentence = ""
i = len(words) - 1
while i >= 0:
    rev_sentence += words[i]
    if i != 0:
       rev_sentence += " "
    
    i -= 1

print("Sentence with words reversed:",rev_sentence) 