N = int(input())

board = [[" " for _ in range(2 * N)] for _ in range(N)]


def solve(x, y, size):
    # 크기가 3 -> 가작 작을 때 삼각형
    if size == 3:
        board[y][x] = "*"
        board[y + 1][x - 1] = "*"
        board[y + 1][x + 1] = "*"
        for k in range(-2, 3):
            board[y + 2][x + k] = "*"
    else:
        new_size = size // 2
        solve(x, y, new_size)
        solve(x - new_size, y + new_size, new_size)
        solve(x + new_size, y + new_size, new_size)


solve(N - 1, 0, N)

for b in board:
    print("".join(b))
