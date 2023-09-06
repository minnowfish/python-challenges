def converter(s):
    vowels = ["a", "e", "i", "o","u"]
    constanants = []
    for i in range(len(s)):
        if s[i].lower() not in vowels and s[i] not in constanants:
            constanants.append(s[i])
    
    for i in constanants:
        s = s.replace(i, i+"o"+i)
    print(s)

inputString = input("Message to translate to Rövarspråket:")
converter(inputString)
