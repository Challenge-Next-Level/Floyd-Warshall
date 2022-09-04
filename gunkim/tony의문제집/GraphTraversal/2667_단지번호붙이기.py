import sys
from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()[:-1]))

visit = [[False for _ in range(n)] for _ in range(n)]
dir = [[0,1], [0,-1], [1,0], [-1,0]]
count = 0


def bfs(y, x):
    cnt = 0
    dq = deque([[y,x]])
    visit[y][x] = True
    while dq:
        sy, sx = dq.popleft()
        cnt += 1
        for dy, dx in dir:
            ny, nx = sy+dy, sx+dx
            if 0<=ny<n and 0<=nx<n and board[ny][nx] == '1' and visit[ny][nx] is False:
                visit[ny][nx] = True
                dq.append([ny, nx])
    return cnt


answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and visit[i][j] is False:
            count += 1
            answer.append(bfs(i, j))
print(count)
answer.sort()
for a in answer:
    print(a)