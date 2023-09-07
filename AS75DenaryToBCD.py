denary = input("Insert a denary number")
BCD = ""

for i in denary:
    binary = format(int(i),'b')
    while len(binary)!= 4:
        binary = '0'+binary
    BCD += binary

print(BCD)
