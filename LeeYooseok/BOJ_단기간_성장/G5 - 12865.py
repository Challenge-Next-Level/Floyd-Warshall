N, K = map(int, input().split())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

item_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    W, V = item_list[i]

    for k in range(K + 1):
        if k < W:
            dp[i + 1][k] = dp[i][k]
        else:
            dp[i + 1][k] = max(dp[i][k], dp[i][k - W] + V)

print(dp[-1][-1])