import sys

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

board = list()
start_x, start_y = 0, 0
for _y in range(n):
    x_board = list(map(int, input().split()))
    for _x in range(m):
        if x_board[_x] == 2:
            start_x, start_y = _x, _y
        elif x_board[_x] == 1:
            x_board[_x] = -1
    board.append(x_board)

visited = [[False for _ in range(m)] for _ in range(n)]
que = deque([[start_x, start_y, 0]])
visited[start_y][start_x] = True
board[start_y][start_x] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    now_x, now_y, move_cnt = que.popleft()

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not (0 <= new_x < m) or not (0 <= new_y < n):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] != -1:
            continue

        que.append([new_x, new_y, move_cnt + 1])
        board[new_y][new_x] = move_cnt + 1
        visited[new_y][new_x] = True

for b in board:
    print(*b)