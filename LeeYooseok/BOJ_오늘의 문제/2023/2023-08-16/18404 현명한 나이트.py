from collections import deque

N, M = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
N_y, N_x = map(int, input().split())
N_y -= 1
N_x -= 1
visited[N_y][N_x] = 1

dq = deque()
dq.append([N_y, N_x, 0])

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

M_list = list()
for _ in range(M):
    y, x = map(int, input().split())
    y -= 1
    x -= 1

    board[y][x] = 1e9
    M_list.append([y, x])

cnt = 0

while deque:
    now_y, now_x, now_cnt = dq.popleft()

    if board[now_y][now_x] == 1e9:
        cnt += 1
        board[now_y][now_x] = now_cnt

    if cnt == M:
        break

    for i in range(8):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < N) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x] != 0:
            continue

        visited[new_y][new_x] = 1
        dq.append([new_y, new_x, now_cnt + 1])

for y, x in M_list:
    print(board[y][x], end = " ")