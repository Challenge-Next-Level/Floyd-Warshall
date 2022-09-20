import sys
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
dir = [[0,1], [0,-1], [1,0], [-1,0]]

h, w, sr, sc, fr, fc = map(int, sys.stdin.readline().split())
sr -= 1
sc -= 1
fr -= 1
fc -= 1
visit = [[False for _ in range(m)] for _ in range(n)]


def bfs(r, c, gr, gc):
    dq = deque([[r, c, 0]])
    visit[r][c] = True
    while dq:
        y, x, cnt = dq.popleft()
        if y == gr and x == gc: # 도착
            return cnt
        for dy, dx in dir: # 상하좌우 이동
            ny, nx = y + dy, x + dx
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] is False and 0<=ny+h-1<n and 0<=nx+w-1<m:
                flag = 0
                if dy == 0:
                    if dx == 1: # 우 이동
                        for i in range(ny, ny+h):
                            if board[i][nx+w-1] == 1:
                                flag = 1
                                break
                    elif dx == -1: # 좌 이동
                        for i in range(ny, ny+h):
                            if board[i][nx] == 1:
                                flag = 1
                                break
                elif dx == 0:
                    if dy == 1: # 하 이동
                        for i in range(nx, nx+w):
                            if board[ny+h-1][i] == 1:
                                flag = 1
                                break
                    elif dy == -1: # 상 이동
                        for i in range(nx, nx+w):
                            if board[ny][i] == 1:
                                flag = 1
                                break
                if flag == 0:
                    visit[ny][nx] = True
                    dq.append([ny, nx, cnt+1])
    return -1


print(bfs(sr, sc, fr, fc))