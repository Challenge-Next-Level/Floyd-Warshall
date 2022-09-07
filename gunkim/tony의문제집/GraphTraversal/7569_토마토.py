import sys
from collections import deque

m, n , h = map(int, input().split())
board = [[] for _ in range(h)]
location = []
for i in range(h):
    for j in range(n):
        tomato = list(map(int, sys.stdin.readline().split()))
        board[i].append(tomato)
        for k in range(m):
            if tomato[k] == 1:
                location.append([i,j,k])
dir = [[0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]


def bfs():
    answer = 0
    dq = deque([])
    for i in range(len(location)):
        z, y, x = location[i]
        dq.append([z, y, x, 0]) # 좌표, 0일차
    while dq:
        sz, sy, sx, date = dq.popleft()
        for dz, dy, dx in dir:
            nz, ny, nx = sz + dz, sy + dy, sx + dx
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and board[nz][ny][nx] == 0 and visit[nz][ny][nx] is False:
                visit[nz][ny][nx] = True
                dq.append([nz, ny, nx, date+1])
        if len(dq) == 0:
            answer = date
    return answer


def check(result):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0 and visit[i][j][k] is False:
                    return -1
    return result


print(check(bfs()))