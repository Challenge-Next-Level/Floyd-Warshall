import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# dp[i][j] =  i챕터까지 확인했을 때, j일이 남았을 때 읽을 수 있는 최대 페이지 수
dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    d, p = map(int, input().split())
    for j in range(1, N + 1):
        if j - d >= 0:
            dp[i][j] = max(dp[i - 1][j - d] + p, dp[i - 1][j])  # 현재 입력받은 챕터를 읽음, 읽지 않음
        dp[i][j] = max(dp[i - 1][j], dp[i][j])


print(dp[-1][-1])