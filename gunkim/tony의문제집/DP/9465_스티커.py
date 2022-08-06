import sys

t = int(input())
for _ in range(t):
    n = int(input())
    board = [[] for _ in range(2)]
    for i in range(2):
        board[i] = list(map(int, sys.stdin.readline().split()))

    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = board[0][0]
    dp[0][2] = board[1][0]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], max(dp[i-1][1], dp[i-1][2]))
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + board[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + board[1][i]

    print(max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])))