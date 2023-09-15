n = int(input())
num_list = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
dp[0][0] = num_list[0]

ans = num_list[0]
for i in range(1, n):
    # 아무런 원소를 제거하지 않았을때
    dp[i][0] = max(dp[i - 1][0] + num_list[i], num_list[i])

    # 특정 원소를 제거한 경우 -> 1. i 번째 원소를 제거하는 경우, 2. i 번째 이전에서 이미 특정 원소를 제거하여 i 번째 원소를 사용해야 하는 경우
    dp[i][1] = max(dp[i-1][0], dp[i - 1][1] + num_list[i])

    ans = max(ans, dp[i][0], dp[i][1])

print(ans)