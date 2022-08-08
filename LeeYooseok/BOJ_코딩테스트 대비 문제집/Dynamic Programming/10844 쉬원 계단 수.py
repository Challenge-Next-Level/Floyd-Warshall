n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]
# n이 1일때 계단 개수
for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, n+1):
    for k in range(10):
        # 0으로 올 수 있는 방법 - 이전 단계가 1
        if k == 0:
            dp[j][k] = dp[j-1][1]
        # 9로 올 수 있는 방법 - 이전 단계가 8
        elif k == 9:
            dp[j][k] = dp[j-1][8]
        # 다른 경우 - 이전 단계가 k-1, k+1
        else:
            dp[j][k] = dp[j-1][k-1] + dp[j-1][k+1]

print(sum(dp[n]) % 1000000000)


