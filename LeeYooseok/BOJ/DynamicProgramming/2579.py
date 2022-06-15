N = int(input())

stair_list = [0 for _ in range(301)]
for n in range(N):
    stair_list[n] = int(input())

dp = [0 for _ in range(301)]

dp[0] = stair_list[0]
dp[1] = stair_list[0] + stair_list[1]
dp[2] = max(stair_list[0] + stair_list[2], stair_list[1] + stair_list[2])

for i in range(3, N):
    # (2, 1) (2) 비교
    dp[i] = max(dp[i-3] + stair_list[i - 1] + stair_list[i], dp[i - 2] + stair_list[i])

print(dp[N-1])