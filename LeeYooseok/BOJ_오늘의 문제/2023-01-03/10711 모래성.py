import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
board = list()
que = deque()
for _y in range(H):
    y_board = list(input())

    for _x in range(W):
        if y_board[_x] == '.':
            que.append([_x, _y])
            y_board[_x] = 0
        else:
            y_board[_x] = int(y_board[_x])
    board.append(y_board)

# 8방향
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

visited = [[0 for _ in range(W)] for _ in range(H)]
answer = 0

while que:
    now_x, now_y = que.popleft()

    for i in range(8):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < W) or not(0 <= new_y < H):
            continue

        if board[new_y][new_x] > 0:
            board[new_y][new_x] -= 1
            if board[new_y][new_x] == 0:
                visited[new_y][new_x] = visited[now_y][now_x] + 1
                answer = max(answer, visited[new_y][new_x])
                que.append([new_x, new_y])

print(answer)