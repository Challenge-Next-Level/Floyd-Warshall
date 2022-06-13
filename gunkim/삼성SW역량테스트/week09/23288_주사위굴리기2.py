import sys

n, m, k = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dir = [[0,1], [1,0], [0,-1], [-1,0]] # 동남서북
dice = [2, # 뒷면
        [4,1,3], # 왼면,윗면,오른면
        5, # 앞면
        6]
y, x, di = 0, 0, 0 # 현재 y,x좌표 및 방향


def move(d): # 주사위 이동 직접 구현
    if d == 0: # 동쪽 이동
        temp = dice[1][2]
        dice[1] = [dice[3]] + dice[1][:2]
        dice[3] = temp
    elif d == 2: # 서쪽 이동
        temp = dice[1][0]
        dice[1] = dice[1][1:] + [dice[3]]
        dice[3] = temp
    elif d == 1: # 남쪽 이동
        temp = dice[2]
        dice[2] = dice[1][1]
        dice[1][1] = dice[0]
        dice[0] = dice[3]
        dice[3] = temp
    elif d == 3: # 북쪽 이동
        temp = dice[0]
        dice[0] = dice[1][1]
        dice[1][1] = dice[2]
        dice[2] = dice[3]
        dice[3] = temp


def dfs(sy, sx, num, visit, idx): # 갈 수 있는 모든 곳을 탐색
    result[idx] += 1
    for dy, dx in dir:
        ny, nx = sy + dy, sx + dx
        if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and board[ny][nx] == num:
            visit[ny][nx] = 1
            dfs(ny, nx, num, visit, idx)
    return


result = [0 for _ in range(k)]
answer = 0
for i in range(k):
    # 1. 주사위 이동
    ny, nx = y + dir[di][0], x + dir[di][1]
    if not (0 <= ny < n and 0 <= nx < m):
        di = (di + 2) % 4
        ny, nx = y + dir[di][0], x + dir[di][1]
    move(di)
    # 2. 점수 획득
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[ny][nx] = 1
    dfs(ny, nx, board[ny][nx], visited, i)
    answer += result[i] * board[ny][nx]
    # 3. 이동 방향 결정
    if dice[3] > board[ny][nx]:
        di = (di + 1) % 4
    elif dice[3] < board[ny][nx]:
        di = (di + 3) % 4
    y, x = ny, nx # 좌표 갱신

print(answer)