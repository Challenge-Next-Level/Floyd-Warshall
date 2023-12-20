N, K = map(int, input().split())

point = list()
for _ in range(N):
    x, y = map(int, input().split())
    point.append([x, y])

distance = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        distance[i][j] = abs(point[i][0] - point[j][0]) + abs(point[i][1] - point[j][1])

dp = [[1e9 for _ in range(N)] for _ in range(K + 1)]

# K = 0 -> 아무것도 안 건너 뛸때
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + distance[i - 1][i]

# k = 1, 2, ... k
for i in range(1, K + 1):
    dp[i][0], dp[i][1] = 0, dp[i - 1][1]
    dp[i][i] = distance[0][i]
    for j in range(1, N):
        for m in range(i, 0, -1):
            if j - m - 1 < 0:
                continue
            # 현재 값, K 값을 더 적게 사용하는 경우, K 값 만큼 건너 뛴 경우
            dp[i][j] = min(dp[i][j], dp[i - m][j - m - 1] + distance[j][j - m - 1], dp[i][j - 1] + distance[j - 1][j])

print(dp[-1][-1])