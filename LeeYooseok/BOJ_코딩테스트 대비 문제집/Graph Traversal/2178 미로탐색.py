import sys
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input())) for _ in range(N)]

visited = [list(False for _ in range(M)) for _ in range(N)]

result = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()
que.append([1, 0, 0])

while que:
    now_cnt, now_x, now_y = que.popleft()

    if now_x == M - 1 and now_y == N - 1:
        result = min(now_cnt, result)
        continue

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not (0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] == 0:
            continue

        visited[new_y][new_x] = True
        que.append([now_cnt + 1, new_x, new_y])

print(result)