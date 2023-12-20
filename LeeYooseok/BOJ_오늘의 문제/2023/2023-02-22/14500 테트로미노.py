import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
visited = [[False] * M for _ in range(N)]

def dfs(now_x, now_y, cnt, total):
    global answer
    if cnt == 4:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < M) or not(0 <= new_y < N):
                continue

            if visited[new_y][new_x]:
                continue

            if cnt == 2:
                visited[new_y][new_x] = True
                dfs(now_x, now_y, cnt + 1, total + board[new_y][new_x])
                visited[new_y][new_x] = False
            visited[new_y][new_x] = True
            dfs(new_x, new_y, cnt + 1, total + board[new_y][new_x])
            visited[new_y][new_x] = False

for _y in range(N):
    for _x in range(M):
        visited[_y][_x] = True
        dfs(_x, _y, 1, board[_y][_x])
        visited[_y][_x] = False

print(answer)