import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(C)] for _ in range(R)]

answer = 0


def DFS(x, y):
    stack = [[x, y]]
    visited[y][x] = True

    while stack:
        now_x, now_y = stack.pop()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]
            if not (0 <= new_x < C) or not (0 <= new_y < R):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == ".":
                continue

            visited[new_y][new_x] = True
            stack.append([new_x, new_y])


for _y in range(R):
    for _x in range(C):
        if visited[_y][_x]:
            continue

        if board[_y][_x] == ".":
            continue

        answer += 1
        DFS(_x, _y)

print(answer)