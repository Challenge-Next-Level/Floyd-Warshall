import sys

n, m = map(int, sys.stdin.readline().split())
board = []
airCon = []
for i in range(n):
    A = list(map(int, sys.stdin.readline().split()))
    board.append(A)
    for j in range(m):
        if A[j] == 9:
            airCon.append([i,j])
dir = [[0,-1], [-1,0], [0,1], [1,0]] # 서, 북, 동, 남
item = {1:(9,1,9,3),
        2:(0,9,2,9),
        3:(3,2,1,0),
        4:(1,0,3,2)}
visit = [[False] * m for _ in range(n)]


def nextWind(y, x):
    for i in range(4):
        idx = i
        ny, nx = y+dir[idx][0], x+dir[idx][1]
        while True: # 바람이 벽 or 에어컨을 만날때 까지 진행
            if not 0<=ny<n or not 0<=nx<m or board[ny][nx] == 9:
                break
            else:
                visit[ny][nx] = True
                if board[ny][nx] != 0:
                    idx = item[board[ny][nx]][idx]
                    if idx == 9:
                        break
                ny += dir[idx][0]
                nx += dir[idx][1]
    return


# 미리 저장한 에어컨 위치에 대해 바람 방향 탐색
for i in range(len(airCon)):
    y, x = airCon[i]
    visit[y][x] = True
    nextWind(y, x)

# 출력
total = 0
for i in range(n):
    for j in range(m):
        if visit[i][j]:
            total += 1
print(total)