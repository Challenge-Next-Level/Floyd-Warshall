import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if dp[x][y]: return dp[x][y] # 이미 한번 왔다간 경로는 그대로 리턴
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 현재 위치의 최댓값 : 다음 위치 에서 갈 수 있는 곳(다음 위치의 최댓값) + 1
    return dp[x][y]


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
dp = [[0] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)