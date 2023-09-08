list = [93,6428,13,4,72,84,389,10]
flags = 1
while flags > 0:
    flags = 0
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            flags += 1
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp

print(list)
