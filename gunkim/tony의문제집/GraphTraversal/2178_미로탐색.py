# dfs로 시도하면 모든 경로를 탐색해야 하기에 '시간초과' 발생
import sys
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()[:-1]))


visit = [[False for _ in range(m)] for _ in range(n)]
dir = [[0,1], [0,-1], [1,0], [-1,0]]


def bfs(y, x):
    dq = deque([[y,x,1]])
    visit[y][x] = True
    while dq:
        sy, sx, depth = dq.popleft()
        if sy == n-1 and sx == m-1:
            return depth
        for dy, dx in dir:
            ny, nx = sy + dy, sx + dx
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] is False and board[ny][nx] == '1':
                visit[ny][nx] = True
                dq.append([ny,nx,depth+1])
    return -1


answer = bfs(0,0)
print(answer)