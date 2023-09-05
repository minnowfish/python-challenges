def reverse_string(s):
    reversedString = s[::-1]
    return(reversedString)

inputString = input("Insert what you would like to reverse")
results = reverse_string(inputString)
print(results)
