N = int(input())
cost_list = [list(map(int, input().split())) for _ in range(N)]

ans = 1e9

# 첫번째 집을 각각 R, G, B 로 칠하는 경우
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for _ in range(N)]
    dp[0][i] = cost_list[0][i]

    for j in range(1, N):
        dp[j][0] = cost_list[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = cost_list[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = cost_list[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for k in range(3):
        # 마지막이랑, 처음이랑 달라야함
        if i != k:
            ans = min(ans, dp[-1][k])

print(ans)