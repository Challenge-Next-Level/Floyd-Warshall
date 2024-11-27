N = int(input())

board = [["*" for _ in range(N)] for _ in range(N)]


def solve(x, y, size):
    if size == 1:
        board[y + 1][x + 1] = " "
        return
    for _y in range(3):
        for _x in range(3):
            if _x == 1 and _y == 1:
                for y_idx in range(y + size, y + 2 * size):
                    for x_idx in range(x + size, x + 2 * size):
                        board[y_idx][x_idx] = " "
            else:
                solve(x + _x * size, y + _y * size, size // 3)


solve(0, 0, N // 3)

for b in board:
    print("".join(b))
