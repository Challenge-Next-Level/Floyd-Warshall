import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int, input().split())

    x_1, y_1, x_2, y_2 = x_1, M - y_2, x_2, M - y_1

    for _x in range(x_1, x_2):
        for _y in range(y_1, y_2):
            board[_y][_x] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [b[:] for b in board]


def bfs(x, y):
    queue = deque([[x, y]])
    size = 1

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < M):
                continue

            if visited[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = 1
            size += 1
            queue.append([new_x, new_y])

    return size


answer_cnt = 0
size_list = list()
for _y in range(M):
    for _x in range(N):
        if visited[_y][_x] == 0:
            answer_cnt += 1
            visited[_y][_x] = 1
            size_list.append(bfs(_x, _y))
size_list.sort()

print(answer_cnt)
print(*size_list)
