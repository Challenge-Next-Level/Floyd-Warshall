import sys

n = int(input())

stone_list = list()

dp = [sys.maxsize for _ in range(n + 1)]
dp[0] = 0
for idx in range(n):
    s, b = map(int, input())
    stone_list.append([s, b])
    if idx + 1 < n:
        dp[idx + 1] = min(dp[idx + 1], dp[idx] + s)

    if idx + 2 < n:
        dp[idx + 2] = min(dp[idx + 2], dp[idx] + b)

# 매우 큰 점프 적용해보며 최솟값 찾기
K = int(input())
answer = dp[-1]
for i in range(3, n):
    e, dp1, dp2 = dp[i - 3] + K, 1e9, 1e9
    for j in range(i, n - 1):
        if i + 1 <= n:
            dp1 = min(dp1, e + stone_list[j][0])
        if i + 2 <= n:
            dp2 = min(dp2, e + stone_list[j][1])
        e, dp1, dp2 = dp1, dp2, 1e9
    answer = min(answer, e)

print(answer)
