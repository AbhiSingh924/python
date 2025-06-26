str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Strings are not isomorphic.")
else:
    mapping1 = {}
    mapping2 = {}
    is_isomorphic = True

    for i in range(len(str1)):
        ch1 = str1[i]
        ch2 = str2[i]

        if ch1 in mapping1:
            if mapping1[ch1] != ch2:
                is_isomorphic = False
                break
        else:
            mapping1[ch1] = ch2

        if ch2 in mapping2:
            if mapping2[ch2] != ch1:
                is_isomorphic = False
                break
        else:
            mapping2[ch2] = ch1

    if is_isomorphic:
        print("Strings are isomorphic.")
    else:
        print("Strings are not isomorphic.")