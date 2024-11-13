T = int(input())

dp = [1 for _ in range(1001)]
for i in range(1, 1001):
    for j in range(i - 1):
        if (i - j) % 2 != 0:
            continue

        dp[i] += dp[(i - j) // 2]

for _ in range(T):
    print(dp[int(input())])