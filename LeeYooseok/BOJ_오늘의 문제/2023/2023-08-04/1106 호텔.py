C, N = map(int, input().split())

dp = [1e9 for _ in range(C + 101)]
city_list = list()
max_p = 0
for _ in range(N):
    c, p = map(int, input().split())
    dp[p] = min(dp[p], c)
    city_list.append([c, p])

for i in range(1, C + 101):
    min_cost = 1e9

    for c, p in city_list:
        if i - p > 0:
            if dp[i - p] != -1:
                min_cost = min(min_cost, dp[i - p] + c)
    if min_cost != 1e9:
        dp[i] = min(dp[i], min_cost)

print(min(dp[C:]))