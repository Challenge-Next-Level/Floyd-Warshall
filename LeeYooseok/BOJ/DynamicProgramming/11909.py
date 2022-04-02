import sys

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())

heap = []

dp = [[0] * n for _ in range(n)]

# [y][x]
maze = [list(map(int, input().split())) for _ in range(n)]

# i = 세로, j = 가로
for i in range(n):
    for j in range(n):
        # 초기값인 경우
        if i == 0 and j == 0:
            continue
        # y == 0 즉 (j,0)로 오는 방법은 오른쪽 방향으로 이동하는 법 하나밖에 없다.
        elif i == 0:
            # 현재 블럭 < 이전 블럭
            if maze[i][j] < maze[i][j-1]:
                # 그냥 이동 가능
                cost = dp[i][j-1]
            else:
                # 버튼 누르고 이동
                # 이전 까지의 최솟값 + (현재 블럭 - 이전 블럭 + 1)
                cost = dp[i][j-1] + maze[i][j] - maze[i][j-1] + 1

            dp[i][j] = cost

        # x == 0 즉 (0, i)로 오는 방법은 아래로 이동하는 법 하나밖에 없다.
        elif j == 0:
            if maze[i][j] < maze[i-1][j]:
                cost = dp[i-1][j]
            else:
                cost = dp[i-1][j] + maze[i][j] - maze[i-1][j] + 1

            dp[i][j] = cost

        else:
            # (j, i)로 가기 위해 이전 칸에서 오른쪽으로 이동하는 경우
            if maze[i][j] < maze[i][j-1]:
                cost_r = dp[i][j-1]
            else:
                cost_r = dp[i][j-1] + maze[i][j] - maze[i][j-1] + 1

            # (j, i)로 가기 위해 이전 칸에서 아래쪽으로 이동하는 경우
            if maze[i][j] < maze[i-1][j]:
                cost_d = dp[i-1][j]
            else:
                cost_d = dp[i-1][j] + maze[i][j] - maze[i-1][j] + 1

            dp[i][j] = min(cost_r, cost_d)

print(dp[-1][-1])