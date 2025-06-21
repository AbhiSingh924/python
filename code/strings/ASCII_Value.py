str = input("Enter a string: ")
str = str.replace(" ","")
character = ""

print("Character : ASCII Value")
for ch in str:
    if ch not in character:
        character += ch
        print(f"{ch} : {ord(ch)}")