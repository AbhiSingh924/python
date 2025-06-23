str = input("Enter a string:- ")
result = ""

start = 0
while start < len(str) and str[start] == " ":
    start += 1

end = len(str) - 1  
while end < len(str) and str[end] == " ":
    end -= 1
    
i = start
while i <= end:
    if str[i] != " ":
        result += str[i]

    elif len(result) == 0 or result[-1] != " ":
        result += " "
    i += 1
    
print("String without leading and trailing space :- ",result)