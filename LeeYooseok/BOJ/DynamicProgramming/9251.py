import sys

S1 = sys.stdin.readline()
S2 = sys.stdin.readline()

len1 = len(S1)
len2 = len(S2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # 해당 문자열이 같을 시, 해당 문자가 추가되기 전의 칸 + 1
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 다를시, 해당 문자가 추가되기 전의 문자열로 만들 수 있던 최대 길이의 값
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
