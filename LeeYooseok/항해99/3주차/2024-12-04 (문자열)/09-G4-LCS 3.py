S1 = input().rstrip()
S2 = input().rstrip()
S3 = input().rstrip()

dp = [[[0 for _ in range(len(S3) + 1)] for _ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]

for i in range(len(S1)):
    for j in range(len(S2)):
        for k in range(len(S3)):
            if S1[i] == S2[j] and S2[j] == S3[k] and S3[k] == S1[i]:
                dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
            else:
                dp[i + 1][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i + 1][j][k + 1], dp[i + 1][j + 1][k])

print(dp[-1][-1][-1])
