N, K = map(int, input().split())

item_list = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())

    item_list.append([W, V])

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for item_idx in range(1, N + 1):
    for k in range(1, K + 1):

        weight, value = item_list[item_idx]

        # 가방에 넣을 수 없으면
        if k < weight:
            dp[item_idx][k] = dp[item_idx - 1][k] # 위에 값 그대로 가져오기
        # 가방에 넣을 수 있으면
        else:
            # 해당 item 을 안넣거나, 넣거나
            dp[item_idx][k] = max(dp[item_idx - 1][k], dp[item_idx - 1][k - weight] + value)

print(dp[-1][-1])