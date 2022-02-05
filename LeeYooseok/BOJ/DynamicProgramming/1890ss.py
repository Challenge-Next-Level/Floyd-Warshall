"""
- dp 테이블 생성
    - 현재 위치까지 올 수 있는 경우의 수
"""

import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        # 현재 위치로 올 수 있는 경우가 존재 시(현재 위치까지 올 수 있는 경우의 수 != 0),
        now = dp[i][j]
        if now != 0 and not (i == n-1 and j == n-1):
            num = matrix[i][j]
            # 오른쪽 방향
            # 범위 확인
            if j+num < n:
                dp[i][j+num] += now

            # 아래쪽 방향
            # 범위 확인
            if i+num < n:
                dp[i+num][j] += now


print(dp[n-1][n-1])
