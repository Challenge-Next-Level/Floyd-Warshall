# https://breakcoding.tistory.com/366

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(M + 1)]
maxFarm = 0

for _y in range(1, M + 1):
    for _x in range(1, N + 1):
        if not board[_y][_x]:
            dp[_y][_x] = min(dp[_y-1][_x], dp[_y][_x-1], dp[_y-1][_x-1]) + 1 # 자기 기준 위, 왼쪽, 대각선(왼쪽 위) 에 크기 1개를 증가
            maxFarm = max(maxFarm, dp[_y][_x])

print(maxFarm)