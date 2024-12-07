n = int(input())

# 2 - 1, 4 - 2, 5 - 1
dp = [-1, -1, 1, -1, 2, 1]

for i in range(6, n + 1):
    if dp[i - 2] != -1 and dp[i - 5] == -1:
        dp.append(dp[i - 2] + 1)
    elif dp[i - 2] == -1 and dp[i - 5] != -1:
        dp.append(dp[i - 5] + 1)
    elif dp[i - 2] != -1 and dp[i - 5] != -1:
        dp.append(min(dp[i - 2], dp[i - 5]) + 1)
    else:
        dp.append(-1)

print(dp[n])
