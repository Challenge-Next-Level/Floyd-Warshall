N, K = map(int, input().split())

item_list = list()
for _ in range(N):
    W, V = map(int, input().split())
    item_list.append([W, V])

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 모든 아이템들에 대해서
for i in range(1, N + 1):
    # 넣을 수 있는 무게
    item_weight, item_value = item_list[i - 1]

    for j in range(K + 1):
        # item을 담을 수 없다면
        if j < item_weight:
            # item을 담지 않았을 때 최댓값
            dp[i][j] = dp[i - 1][j]
        # item을 담을 수 있다면
        else:
            # max(item을 담지 않았을 때, item을 담았을 때)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_weight] + item_value)

print(dp[-1][-1])
