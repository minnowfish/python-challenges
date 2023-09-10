n = int(input("Width of the board"))
m = int(input("Height of the board"))

board = []

for i in range(m):
    row = []
    board.append(row)
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        else:
            if j % 2 == 0:
                row.append("*")
            else:
                row.append(".")


for i in range(m):
    print(board[i])
