N = int(input())

# 0, 1, 2, 3, 4, 5, 6, 7
dp = [0, 1, 1, 2, 2, 1, 2, 1]

if N > 7:
    for n in range(8, N + 1):
        dp.append(min(dp[n - 1] + 1, dp[n - 2] + 1, dp[n - 5] + 1, dp[n - 7] + 1))

print(dp[N])