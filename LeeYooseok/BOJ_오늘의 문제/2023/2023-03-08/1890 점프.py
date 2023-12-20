N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)] # (x, y)로 올 수 있는 경우의 수

dp[0][0] = 1

for _y in range(N):
    for _x in range(N):
        if board[_y][_x] == 0:
            print(dp[_y][_x])
            break

        now_move = board[_y][_x]
        # 오른쪽으로 이동
        if _x + now_move < N:
            dp[_y][_x + now_move] += dp[_y][_x]
        # 아래로 이동
        if _y + now_move < N:
            dp[_y + now_move][_x] += dp[_y][_x]