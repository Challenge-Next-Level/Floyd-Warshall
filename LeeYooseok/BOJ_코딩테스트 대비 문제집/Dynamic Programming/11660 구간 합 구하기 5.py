# 2차원 배열 구간 합 : https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-11660-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-5
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 계산
for x in range(0, n):
    for y in range(0, n):
        dp[x+1][y+1] = dp[x][y+1] + dp[x+1][y] - dp[x][y] + board[x][y]

for _ in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    print(dp[x_2][y_2] - (dp[x_1 - 1][y_2] + dp[x_2][y_1 - 1] - dp[x_1 - 1][y_1 - 1]))
