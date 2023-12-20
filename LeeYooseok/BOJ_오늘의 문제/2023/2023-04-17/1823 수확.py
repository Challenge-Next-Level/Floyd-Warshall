import sys
input = sys.stdin.readline

N = int(input())
v = [0]+[int(input()) for _ in range(N)]
dp = [[v[i] * N if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]

for left in range(1, N + 1):
    for right in range(left - 1, 0, -1):
        idx = N - left + right
        dp[right][left] = max(dp[right + 1][left] + v[right] * idx, dp[right][left - 1] + v[left]*idx)

print(dp[1][N])