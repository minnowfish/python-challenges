#Exercise 1: Code this up in Python
#Exercise 2: Check out your solution against this spreadsheet. 
number = int(input("Insert the number (excluding checksum)"))
checksum = input("Insert the checksum")
digit = [int(x) for x in str(number)]
length = len(digit)
sum = 0

for i in range(length):
    sum += digit[i]*(length + 1-i)

results = 11 - (sum%11)

if results == 11:
    results = 0
elif results == 10:
    results = "X"

if str(results) == checksum:
    print("Check passed")
else:
    print("Check failed")
