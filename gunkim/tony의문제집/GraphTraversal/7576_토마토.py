import sys
from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for _ in range(m)] for _ in range(n)]
location = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            location.append([i, j])
            visit[i][j] = True

dir = [[1,0], [-1,0], [0,1], [0,-1]]


def bfs():
    answer = 0
    dq = deque([])
    for i in range(len(location)):
        y, x = location[i]
        dq.append([y, x, 0]) # 좌표, 0일차
    while dq:
        sy, sx, date = dq.popleft()
        for dy, dx in dir:
            ny, nx = sy + dy, sx + dx
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0 and visit[ny][nx] is False:
                visit[ny][nx] = True
                dq.append([ny, nx, date+1])
        if len(dq) == 0:
            answer = date
    return answer


def check(result):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and visit[i][j] is False:
                return -1
    return result


result = bfs()
print(check(result))