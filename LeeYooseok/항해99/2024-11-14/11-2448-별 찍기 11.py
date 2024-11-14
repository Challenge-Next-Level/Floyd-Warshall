N = int(input())

# 오르쪽 마지막 열은 비워져있음
board = [[" " for _ in range(2 * N)] for _ in range(N)]

# 시작 기준점 : 삼각형 가운데 위
def solve(x, y, size):
    # 크기가 3 -> 가장 작을때 삼각형
    if size == 3:
        board[y][x] = "*"
        board[y + 1][x - 1] = "*"
        board[y + 1][x + 1] = "*"
        for k in range(-2, 3):
            board[y + 2][x + k] = "*"
    else:
        new_size = size // 2
        # 위 삼각형
        solve(x, y, new_size)
        # 왼쪽 아래 삼각형
        solve(x - new_size, y + new_size, new_size)
        # 오른쪽 아래 삼각형
        solve(x + new_size, y + new_size, new_size)


# 시작점 -> (가운데 가장 위)
solve(N - 1, 0, N)

for b in board:
    print(b)
