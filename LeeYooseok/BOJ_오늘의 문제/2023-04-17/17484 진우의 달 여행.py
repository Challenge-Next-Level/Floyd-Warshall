N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1e9] * 3 for _ in range(M)] for _ in range(N)]

for _y in range(N):
    if _y == 0:
        for _x in range(M):
            for d in range(3):
                dp[_y][_x][d] = board[_y][_x]
    else:
        for _x in range(M):
            if _x == 0:
                dp[_y][_x][0] = min(dp[_y-1][_x+1][1], dp[_y-1][_x+1][2]) + board[_y][_x]
                dp[_y][_x][1] = dp[_y-1][_x][0] + board[_y][_x]
            elif _x == M-1:
                dp[_y][_x][1] = dp[_y-1][_x][2] + board[_y][_x]
                dp[_y][_x][2] = min(dp[_y-1][_x-1][0], dp[_y-1][_x-1][1]) + board[_y][_x]
            else:
                dp[_y][_x][0] = min(dp[_y-1][_x+1][1], dp[_y-1][_x+1][2]) + board[_y][_x]
                dp[_y][_x][1] = min(dp[_y-1][_x][0], dp[_y-1][_x][2]) + board[_y][_x]
                dp[_y][_x][2] = min(dp[_y-1][_x-1][0], dp[_y-1][_x-1][1]) + board[_y][_x]

answer = 1e9
for x in range(M):
    answer = min(min(dp[N-1][x]), answer)
print(answer)