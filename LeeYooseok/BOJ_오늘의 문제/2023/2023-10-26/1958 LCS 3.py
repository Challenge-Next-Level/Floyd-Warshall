text1 = input()
text2 = input()
text3 = input()

dp = [[[0 for _ in range(len(text3) + 1)] for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

for i in range(len(text1)):
    for j in range(len(text2)):
        for k in range(len(text3)):
            if text1[i] == text2[j] and text2[j] == text3[k] and text3[k] == text1[i]:
                dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
            else:
                dp[i + 1][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i + 1][j][k + 1], dp[i + 1][j + 1][k])

print(dp[-1][-1][-1])