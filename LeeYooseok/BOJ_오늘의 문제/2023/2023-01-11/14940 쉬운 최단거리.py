from collections import  deque
n, m = map(int, input().split())

dq = deque()
board = list()
s_x, s_y = 0, 0
for y_idx in range(n):
    y_board = list(map(int, input().split()))
    board.append(y_board)
    for x_idx in range(m):
        if y_board[x_idx] == 2:
            s_x, s_y = x_idx, y_idx
            dq.append([x_idx, y_idx, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

new_board = [[0] * m for _ in range(n)]

while dq:
    now_x, now_y, now_t = dq.popleft() # bfs - popleft, dfs - 재귀 또는 pop

    for i in range(4):
        new_x, new_y, new_t = now_x + dx[i], now_y + dy[i], now_t + 1

        if not(0 <= new_x < m) or not(0 <= new_y < n):
            continue

        if new_board[new_y][new_x] != 0 or (new_y == s_y and new_x == s_x):
            continue

        if board[new_y][new_x] == 0:
            continue

        new_board[new_y][new_x] = new_t
        dq.append([new_x, new_y, new_t])

# 도달할 수 없는 곳 : -1 처리
for _y in range(n):
    for _x in range(m):
        if _y == s_y and _x == s_x:
            continue
        if new_board[_y][_x] == 0 and board[_y][_x] != 0:
            new_board[_y][_x] = -1

for b in new_board:
    print(" ".join(list(map(str, b))))



