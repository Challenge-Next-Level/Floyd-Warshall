# N 의 최댓값 : 11
dp = [0 for _ in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for i in range(5, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])