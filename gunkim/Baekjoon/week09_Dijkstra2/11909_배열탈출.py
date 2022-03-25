# 우선 python3 채점은 시간초과가 발생한다. pypy3로 실행해야 함
# 다익스트라는 모두 시간초과가 발생했다. 특별히 백트래킹을 해야겠다는 부분을 찾지 못해서 그런 것 같다
import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
dp = [[float('inf')] * n for _ in range(n)]


# 전형적인 dp 문제 해결로 풀었다
for y in range(n):
    for x in range(n):
        if y == 0 and x == 0:
            dp[y][x] = 0
        elif y == 0:
            dp[y][x] = dp[y][x - 1]
            if board[y][x - 1] <= board[y][x]:
                dp[y][x] += board[y][x] - board[y][x - 1] + 1
        elif x == 0:
            dp[y][x] = dp[y - 1][x]
            if board[y - 1][x] <= board[y][x]:
                dp[y][x] += board[y][x] - board[y - 1][x] + 1
        else:
            right, down = dp[y][x - 1], dp[y - 1][x]
            if board[y][x - 1] <= board[y][x]:
                right += board[y][x] - board[y][x - 1] + 1
            if board[y - 1][x] <= board[y][x]:
                down += board[y][x] - board[y - 1][x] + 1
            dp[y][x] = min(right, down)

print(dp[-1][-1])