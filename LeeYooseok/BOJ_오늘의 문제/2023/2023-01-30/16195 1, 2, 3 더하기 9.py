T = int(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1 # 1을 숫자 1개로 만드는 경우의 수
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    for j in range(2, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % 1000000009

for _ in range(T):
    n, m = map(int, input().split())
    answer = sum(dp[n][:m + 1]) % 1000000009
    print(answer)
