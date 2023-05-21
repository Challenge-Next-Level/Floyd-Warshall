N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 누적 합
sum_board = [[0] * (N + 1)]
for item in board:
    sum_board.append([0] + item[:])

for _y in range(1, N+1):
    for _x in range(1, N+1):
        sum_board[_y][_x] += sum_board[_y - 1][_x] + sum_board[_y][_x - 1] - sum_board[_y - 1][_x - 1]

answer = -1e9

# 정사각형 체크 -> 크기 1 ~ N
for size in range(1, N + 1):
    for _y in range(N + 1 - size):
        for _x in range(N + 1 - size):
            if _x + size <= N + 1 and _y + size <= N + 1:
                answer = max(sum_board[_y + size][_x + size] - sum_board[_y][_x + size] - sum_board[_y + size][_x] + sum_board[_y][_x], answer)

print(answer)