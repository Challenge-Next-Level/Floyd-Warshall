import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n): # (0,0) 에서 (i,j)까지의 사각형 구간 합을 dp로 저장
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = board[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + board[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i][j]

for _ in range(m): # 구해놓은 dp를 이용하면 문제 풀이는 간단한 수식으로 해결 가능
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    y1 -= 1
    x1 -= 1
    y2 -= 1
    x2 -= 1
    if y1 == 0 and x1 == 0:
        print(dp[y2][x2])
    elif y1 == 0:
        print(dp[y2][x2] - dp[y2][x1-1])
    elif x1 == 0:
        print(dp[y2][x2] - dp[y1-1][x2])
    else:
        print(dp[y2][x2] - dp[y2][x1-1] - dp[y1-1][x2] + dp[y1-1][x1-1])