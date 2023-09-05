def histogram(x):
    for i in x:
        print("*"*i)

list1 = []
for i in range(3):
    number = int(input("Input a number for the histogram"))
    list1.append(number)
histogram(list1)
