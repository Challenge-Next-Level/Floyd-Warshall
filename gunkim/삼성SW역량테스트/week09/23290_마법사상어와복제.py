import sys
import copy

m, s = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(4)] for _ in range(4)] # 격자판
fish = []
for _ in range(m):
    fy, fx, d = map(int, sys.stdin.readline().split())
    fx -= 1
    fy -= 1
    d -= 1
    board[fy][fx].append([d, 1])
    fish.append([fy, fx, d])
sy, sx = map(int, sys.stdin.readline().split())
sy -= 1
sx -= 1
board[sy][sx].append([-1, 2])
shark = [sy, sx]

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(s):
# 1. 모든 물고기에게 복제 마법
    fish_copy = copy.deepcopy(fish)
# 2. 모든 물고기 한 칸 이동
    for f in range(len(fish)):
        y, x, di = fish[f]
        flag = 0
        for j in range(8):
            ny, nx = y + dy[(di + j) % 8], x + dx[(di + j) % 8]
            if 0 <= ny < 4 and 0 <= nx < 4 and (len(board[ny][nx]) == 0 or board[ny][nx][0][1] != 3):
                flag = 1
                fish[f] = [ny, nx, (di + j) % 8]
                board

# 3. 상어가 3칸 이동, 물고기가 있다면 죽음 및 냄새를 남김, 물고기 수 > 사전순

# 4. 2초가 지난 곳 냄새는 사라짐

# 5. 복제 마법 적용