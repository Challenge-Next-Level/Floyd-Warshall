n = int(input())
wine_list = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = wine_list[0]
if n >= 2:
    dp[2] = sum(wine_list[:2])

for idx in range(3, n + 1):
    dp[idx] = max(dp[idx-1],
                  dp[idx-2] + wine_list[idx - 1],
                  dp[idx-3] + wine_list[idx - 2] + wine_list[idx - 1])

print(dp[-1])