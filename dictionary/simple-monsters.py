f = open('monsters_simple.txt', 'r')

monsters = {}
next(f)
for line in f:
    line_info = line.split(',')
    monsters[line_info[0]] = line_info[1][:-1]

def search(monsters, name) -> str:
    if name in monsters:
        print(f"{name} is a {monsters[name]}")
        return
    print("monster cannot be found")

name = input("Insert Monster's Name: ")
search(monsters, name.title())
f.close()
