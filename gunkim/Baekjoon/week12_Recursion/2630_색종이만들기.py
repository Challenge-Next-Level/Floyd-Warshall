import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
blue, white = 0, 0


def cut_recursion(size, y, x):
    global white, blue
    if size == 1:
        if board[y][x] == 0:
            white += 1
        else:
            blue += 1
        return
    total = 0
    for i in range(size):
        for j in range(size):
            total += board[y + i][x + j]
    if total == 0:
        white += 1
    elif total == size * size:
        blue += 1
    else:
        go = size // 2
        cut_recursion(go, y, x)
        cut_recursion(go, y, x + go)
        cut_recursion(go, y + go, x)
        cut_recursion(go, y + go, x + go)
    return


cut_recursion(n, 0, 0)
print(white)
print(blue)