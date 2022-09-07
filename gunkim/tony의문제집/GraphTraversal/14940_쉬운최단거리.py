import sys
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for _ in range(m)] for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]

sy, sx = -1, -1
for i in range(n):
    if sy != -1:
        break
    for j in range(m):
        if board[i][j] == 2:
            sy, sx = i, j
            break


def bfs(y, x):
    dq = deque([[y, x, 0]])
    visit[y][x] = True
    distance[y][x] = 0
    while dq:
        ty, tx, time = dq.popleft()
        for dy, dx in dir:
            ny, nx = ty + dy, tx + dx
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] is False and board[ny][nx] == 1:
                visit[ny][nx] = True
                distance[ny][nx] = time + 1
                dq.append([ny, nx, time+1])
    return


bfs(sy, sx)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            distance[i][j] = 0
for i in range(n):
    print(' '.join(list(map(str, distance[i]))))