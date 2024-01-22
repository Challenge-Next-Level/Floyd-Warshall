from collections import deque

N, M, K = map(int, input().split())

board = [['.' for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())

    board[r - 1][c - 1] = '#'

answer = 0

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global answer

    queue = deque([[x, y]])
    visited[y][x] = True

    size = 1

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < M) or not(0 <= new_y < N):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == '#':
                size += 1
                visited[new_y][new_x] = True
                queue.append([new_x, new_y])

    answer = max(answer, size)


for _y in range(N):
    for _x in range(M):
        if board[_y][_x] == '#':
          dfs(_x, _y)
print(answer)