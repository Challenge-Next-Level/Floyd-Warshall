import sys

input = sys.stdin.readline

from collections import deque

board = list()

B_x, B_y = 0, 0
L_x, L_y = 0, 0

for _y in range(10):
    x_board = list(input())
    for _x in range(10):
        if x_board[_x] == "B":
            B_x, B_y = _x, _y
        if x_board[_x] == "L":
            L_x, L_y = _x, _y
    board.append(x_board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(10)] for _ in range(10)]
queue = deque(list())

queue.append([L_x, L_y, 0])
visited[L_y][L_x] = True

while queue:
    now_x, now_y, move_cnt = queue.popleft()
    if now_x == B_x and now_y == B_y:
        print(move_cnt - 1)
        break

    for i in range(4):
        next_x, next_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= next_x < 10) or not(0 <= next_y < 10):
            continue

        if visited[next_y][next_x]:
            continue

        if board[next_y][next_x] == "R":
            continue

        visited[next_y][next_x] = True
        queue.append([next_x, next_y, move_cnt + 1])