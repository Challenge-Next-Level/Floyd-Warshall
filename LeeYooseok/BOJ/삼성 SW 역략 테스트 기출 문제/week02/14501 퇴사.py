n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if schedules[i][0] + i + 1 > n + 1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], schedules[i][1] + dp[i+schedules[i][0]])

print(dp[0])