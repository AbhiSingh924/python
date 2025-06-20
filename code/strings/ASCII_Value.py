text = input("Enter a string: ")

print("Character : ASCII Value")
for ch in text:
    print(f"{ch} : {ord(ch)}")