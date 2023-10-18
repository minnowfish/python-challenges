userInput = input("Input Number")
numbers = [int(x) for x in userInput.split(",")]

minDifference = abs(numbers[1] - numbers[0])

for i in range(1,len(numbers)-1):
    print(i)
    difference = abs(numbers[i+1] - numbers[i])
    minDifference = min(difference, minDifference)

print(f"min difference is: {minDifference}")
