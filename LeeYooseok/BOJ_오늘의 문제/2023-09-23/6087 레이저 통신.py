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

visited = [[1e9] * W for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(C_loc):
    queue = deque([C_loc])
    visited[C_loc[1]][C_loc[0]] = 0

    while queue:
        now_x, now_y = queue.popleft()
        now_val = visited[now_y][now_x]

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            while True:
                if not(0 <= new_x < W) or not(0 <= new_y < H):
                    break

                if board[new_y][new_x] == "*":
                    break

                if visited[new_y][new_x] < now_val + 1:
                    break

                queue.append([new_x, new_y])
                visited[new_y][new_x] = now_val + 1

                new_x, new_y = new_x + dx[i], new_y + dy[i]


bfs(C_loc_list[0])
print(visited[C_loc_list[1][1]][C_loc_list[1][0]] -1)