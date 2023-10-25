# visited 에 방향 추가
from collections import deque

W, H = map(int, input().split())

board = list()
C_loc_list = list()
for _y in range(H):
    x_board = input()
    for _x in range(W):
        if x_board[_x] == 'C':
            C_loc_list.append([_x, _y])
    board.append(x_board)
visited = [[[1e9] * 4 for _ in range(W)] for _ in range(H)]

# 서-북-동-남
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(C_loc):
    queue = deque()
    for i in range(4):
        new_x, new_y = C_loc[0] + dx[i], C_loc[1] + dy[i]

        if not (0 <= new_x < W) or not (0 <= new_y < H):
            continue

        if board[new_y][new_x] == "*":
            continue

        queue.append([new_x, new_y, i])
        visited[new_y][new_x][i] = 0

    while queue:
        now_x, now_y, now_dir = queue.popleft()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]
            now_val = visited[now_y][now_x][now_dir]

            if not (0 <= new_x < W) or not (0 <= new_y < H):
                continue

            if board[new_y][new_x] == "*":
                continue

            if now_dir == 0 or now_dir == 2:
                if i == 1 or i == 3:
                    now_val += 1
            else:
                if i == 0 or i == 2:
                    now_val += 1

            if visited[new_y][new_x][i] == 1e9:
                visited[new_y][new_x][i] = now_val
                queue.append([new_x, new_y, i])
            else:
                # 방문을 했는데 이전 거울 개수보다 더 작을때,
                if visited[new_y][new_x][i] > now_val:
                    visited[new_y][new_x][i] = now_val
                    queue.append([new_x, new_y, i])


bfs(C_loc_list[0])

print(min(visited[C_loc_list[1][1]][C_loc_list[1][0]]))
