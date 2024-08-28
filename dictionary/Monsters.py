f = open("Monsters.txt", "r")

Monsters = {}

for line in f:
    line_info = line.split(',', 4)

    Monsters[line_info[1]] = {'id':line_info[0], 'origin': line_info[2], 'description': line_info[3], 'stats': line_info[4][:-1] }

print(Monsters)

f.close()
