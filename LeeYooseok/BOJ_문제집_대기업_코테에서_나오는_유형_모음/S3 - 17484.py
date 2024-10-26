import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1e9, 1e9, 1e9] for _ in range(M)] for _ in range(N)]

# 초기값
for _x in range(M):
    dp[0][_x] = [board[0][_x] for _ in range(3)]

for _y in range(1, N):
    for _x in range(M):
        if _x == 0:
            dp[_y][_x][0] = board[_y][_x] + min(dp[_y - 1][_x + 1][1], dp[_y - 1][_x + 1][2])
            dp[_y][_x][1] = board[_y][_x] + min(dp[_y - 1][_x][0], dp[_y - 1][_x][2])
        elif _x == M - 1:
            dp[_y][_x][1] = board[_y][_x] + min(dp[_y - 1][_x][0], dp[_y - 1][_x][2])
            dp[_y][_x][2] = board[_y][_x] + min(dp[_y - 1][_x - 1][0], dp[_y - 1][_x - 1][1])
        else:
            dp[_y][_x][0] = board[_y][_x] + min(dp[_y - 1][_x + 1][1], dp[_y - 1][_x + 1][2])
            dp[_y][_x][1] = board[_y][_x] + min(dp[_y - 1][_x][0], dp[_y - 1][_x][2])
            dp[_y][_x][2] = board[_y][_x] + min(dp[_y - 1][_x - 1][0], dp[_y - 1][_x - 1][1])


answer = 1e9
for _x in range(M):
    answer = min(answer, dp[N - 1][_x][0], dp[N - 1][_x][1], dp[N - 1][_x][2])

print(answer)