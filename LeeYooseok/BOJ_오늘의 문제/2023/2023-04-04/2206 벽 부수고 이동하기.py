from collections import deque

N, M = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(N)]

visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]

que = deque()
que.append([0, 0, 0, 1])
visited[0][0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    now_x, now_y, now_k, now_t = que.popleft()

    if now_x == M - 1 and now_y == N - 1:
        print(now_t)
        exit()

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if now_k == 1 and board[new_y][new_x] == 1:
            continue

        if board[new_y][new_x] == 1:
            new_k = now_k + 1
        else:
            new_k = now_k

        if visited[new_y][new_x][new_k] != -1 and visited[new_y][new_x][new_k] <= now_t + 1:
            continue

        visited[new_y][new_x][new_k] = now_t + 1
        que.append([new_x, new_y, new_k, now_t + 1])

print(-1)

