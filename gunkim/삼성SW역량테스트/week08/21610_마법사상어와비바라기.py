import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

move = []
for _ in range(m):
    move.append(list(map(int, sys.stdin.readline().split())))

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dir = [[-1,-1], [-1,1], [1,-1], [1,1]] # 대각선 이동
cloud = deque([[n-1,0], [n-1,1], [n-2,0], [n-2,1]]) # 구름들의 좌표를 저장


for i in range(m):
    d, s = move[i]
    s = s % n
    length = len(cloud)
    visit = [[0 for _ in range(n)] for _ in range(n)] # 구름이 이동한 곳의 좌표를 저장(시간을 줄이기 위함)
    # 1. 구름이 d방향으로 s칸 이동
    for cnt in range(length):
        a, b = cloud.popleft() # 3. 구름이 사라진다
        y, x = a + dy[d] * s, b + dx[d] * s
        if y >= n:
            y = y % n
        elif y < 0:
            y += n
        if x >= n:
            x = x % n
        elif x < 0:
            x += n
        board[y][x] += 1 # 2. 물의 양 증가
        cloud.append([y, x])
        visit[y][x] = 1
    # 4. 물복사버그 마법(대각선 방향 물이 있는 바구니 수 만큼 물 증가)
    for my, mx in cloud:
        count = 0
        for d in dir:
            ny, nx = my + d[0], mx + d[1]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                count += 1
        board[my][mx] += count
    # 5. 물의 양이 2이상인 곳에 구름 생성 및 물 감소(바로 앞에서 구름이 사라진 칸에서는 생성x)
    length = len(cloud)
    for a in range(n):
        for b in range(n):
            if board[a][b] >= 2 and visit[a][b] == 0:
                cloud.append([a, b])
                board[a][b] -= 2
    for cnt in range(length):
        cloud.popleft()

answer = 0
for i in range(n):
    answer += sum(board[i])
print(answer)