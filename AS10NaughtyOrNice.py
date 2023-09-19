def naughtyornice():
    vowels = "aeiou"
    doubleLetter = False
    badStrings = ["ab","cd","pq","xy"]
    letters = []
    vowelCount = 0

    string = input("Insert text")
    for i in range(len(string)):
        if string[i] in vowels:
            vowelCount += 1
        letters.append(string[i])
        if i != 0 and letters[i] == letters[i-1]:
            doubleLetter = True
    if vowelCount < 3:
        return "naughty"
    for i in badStrings:
        if i in string:
            return "naughty"
    if doubleLetter == True:
        return "nice"
    else:
        return "naughty"


print(naughtyornice())
