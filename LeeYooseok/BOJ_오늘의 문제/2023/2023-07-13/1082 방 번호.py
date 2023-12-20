N = int(input())

price_list = list(map(int, input().split()))

M = int(input())

dp = [-1e9 for _ in range(M + 1)]
for i in range(N - 1, -1, -1):
    price = price_list[i]

    for j in range(price, M + 1):
        dp[j] = max(dp[j - price] * 10 + i, i, dp[j])

print(dp[M])