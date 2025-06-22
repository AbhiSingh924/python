str = input("Please enter a string as an input:- ")

wordExe = input("Please enter the Exesting word that you want to replace:- ")
wordNew = input("Enter the new Word that you want to replace with:- ")

str = str.replace(wordExe, wordNew)

print("New string after replacement is: ")
print(str)