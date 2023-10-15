#I didn't notice this was A2 level and not AS

def addDigits(num):
    if num < 10:
        return(num)
    digit = num%10
    remaining = num//10
    return digit + addDigits(remaining)

total = 0
number = int(input("Number: "))
print(addDigits(number))
