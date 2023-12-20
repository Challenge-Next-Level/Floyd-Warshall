N = int(input())
card_price = list(map(int, input().split()))

dp = [card_price[0] * i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(i + 1):
        dp[i] = min(dp[i], dp[i - j] + card_price[j - 1])

print(dp[-1])