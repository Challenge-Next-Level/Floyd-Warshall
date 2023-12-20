n = int(input())
num_list = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]

# 0번째 원소 초기화
# 0번째 원소 사용
dp[0][0] = num_list[0]

# 0번째 원소 삭제
# dp[1][0] = 0
answer = -1e9
for i in range(1, n):
    dp[0][i] = max(num_list[i], dp[0][i - 1] + num_list[i])

    dp[1][i] = max(dp[1][i - 1] + num_list[i], dp[0][i - 1])

    answer = max(answer, dp[0][i], dp[1][i])

print(answer)