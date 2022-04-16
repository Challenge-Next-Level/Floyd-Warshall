n = int(input())
board = [['*'] * n for _ in range(n)]


def star_recursion(size, y, x):
    if size <= 1:
        return
    go = size // 3
    ny, nx = y + go, x + go
    for i in range(go):
        for j in range(go):
            board[ny + i][nx + j] = ' '

    star_recursion(go, y, x)
    star_recursion(go, y, x + go)
    star_recursion(go, y, x + go * 2)

    star_recursion(go, y + go, x)
    star_recursion(go, y + go, x + go * 2)

    star_recursion(go, y + go * 2, x)
    star_recursion(go, y + go * 2, x + go)
    star_recursion(go, y + go * 2, x + go * 2)
    return


star_recursion(n, 0, 0)
for i in range(n):
    print(''.join(board[i]))