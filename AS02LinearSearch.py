list = ["Java", "C++", "C#", "Javascript", "Python", "PHP","CSS", "HTML"]
found = False

for i in range(len(list)):
    if list[i] == "Python":
        found = True
        print("Python was found at index",i)
        break

if found == False:
    print("Python is not in the list")
