N = int(input())

board = [[" " for _ in range(1 + 4 * (N - 1))] for _ in range(1 + 4 * (N - 1))]

def solve(n, x, y):
    if n == 1:
        board[y][x] = '*'
        return

    length = 1 + 4 * (n - 1)

    for i in range(length):
        # 위
        board[y][x + i] = "*"
        # 왼쪽
        board[y + i][x] = "*"
        # 아래
        board[y + length - 1][x + i] = "*"
        # 오른쪽
        board[y + i][x + length - 1] = "*"

    solve(n - 1, x + 2, y + 2)

solve(N, 0, 0)

for b in board:
    print(''.join(b))