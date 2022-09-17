import sys
from collections import deque, defaultdict

K = int(input())

W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]

# 말 사용 횟수, 현재 이동 횟수
visited = [[defaultdict() for _ in range(W)] for _ in range(H)]

m_x = [-1, 1, 0, 0]
m_y = [0, 0, -1, 1]

h_x = [-2, -1, 1, 2, -2, -1, 1, 2]
h_y = [-1, -2, -2, -1, 1, 2, 2, 1]

que = deque()
que.append([0, 0, 0, 0])
visited[0][0][0] = 0

answer = sys.maxsize

while que:
    now_x, now_y, now_k, now_t = que.popleft()

    if now_x == W-1 and now_y == H-1:
        answer = min(answer, now_t)
        print(answer)
        exit()

    if now_k < K:
        for h in range(8):
            new_x, new_y = now_x + h_x[h], now_y + h_y[h]

            if not(0 <= new_x < W) or not(0 <= new_y < H):
                continue

            if now_k + 1 in visited[new_y][new_x].keys():
                if visited[new_y][new_x][now_k + 1] <= now_t + 1:
                    continue

            if board[new_y][new_x] == 1:
                continue

            visited[new_y][new_x][now_k + 1] = now_t + 1
            que.append([new_x, new_y, now_k + 1, now_t + 1])

    for m in range(4):
        new_x, new_y = now_x + m_x[m], now_y + m_y[m]

        if not(0 <= new_x < W) or not(0 <= new_y < H):
            continue

        if now_k in visited[new_y][new_x].keys():
            if visited[new_y][new_x][now_k] <= now_t + 1:
                continue

        if board[new_y][new_x] == 1:
            continue

        visited[new_y][new_x][now_k] = now_t + 1
        que.append([new_x, new_y, now_k, now_t + 1])


print(-1)