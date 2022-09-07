from collections import deque

N, M = map(int, input().split())

board = list()

que = deque()
for _y in range(N):
    x_board = list(map(int, input().split()))
    board.append(x_board)
    for _x in range(M):
        if x_board[_x] == 2:
            que.append([0, _x, _y])

        if x_board[_x] != 0:
            board[_y][_x] = (N * M + 1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False for _ in range(M)] for _ in range(N)]
visited[que[0][2]][que[0][1]] = True

while que:
    now_t, now_x, now_y = que.popleft()
    board[now_y][now_x] = now_t
    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if board[new_y][new_x] == 0:
            continue

        if visited[new_y][new_x]:
            continue

        if now_t + 1 < board[new_y][new_x]:
            visited[new_y][new_x] = True
            que.append([now_t + 1, new_x, new_y])


for _y in range(N):
    for _x in range(M):
        if not visited[_y][_x] and board[_y][_x] != 0:
            board[_y][_x] = -1

for b in board:
    print(" ".join(list(map(str, b))))