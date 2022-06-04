import copy
import sys

fish_init = [[0 for _ in range(3)] for _ in range(17)] # 물고기 번호마다 [좌표, 방향] 저장
board_init = [] # 보드에 물고기 번호 저장
for i in range(4):
    f = list(map(int, sys.stdin.readline().split()))
    board_init.append([f[0], f[2], f[4], f[6]])
    fish_init[f[0]] = [i, 0, f[1] - 1]
    fish_init[f[2]] = [i, 1, f[3] - 1]
    fish_init[f[4]] = [i, 2, f[5] - 1]
    fish_init[f[6]] = [i, 3, f[7] - 1]
dir = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
answer = 0


def dfs(eat, shark, board, fish):
    global answer
    answer = max(answer, eat)
    fish[board[shark[0]][shark[1]]] = [0,0,-1] # 물고기 잡아먹힘
    board[shark[0]][shark[1]] = 0 # 보드에서 물고기 번호 지우기

    for i in range(1, 17): # 16마리의 물고기 이동
        if fish[i][2] == -1: # 물고기가 죽었다면
            continue
        d = fish[i][2] # 방향 인덱스
        y, x = fish[i][0], fish[i][1] # 물고기의 위치
        while (not 0 <= y + dir[d][0] < 4) or (not 0 <= x + dir[d][1] < 4) or (y + dir[d][0] == shark[0] and x + dir[d][1] == shark[1]): #
            d = (d + 1) % 8
        ny, nx = y + dir[d][0], x + dir[d][1]
        num = board[ny][nx] # 이동하는 곳의 물고기 넘버
        if num != 0: # 물고기 교환
            nd = fish[num][2]
            fish[i] = [ny, nx, d]
            board[ny][nx] = i
            fish[num] = [y, x, nd]
            board[y][x] = num
        else: # 빈곳 이동
            fish[i] = [ny, nx, d]
            board[ny][nx] = i
            board[y][x] = 0

    # 상어 이동
    y, x, d = shark
    for i in range(1, 5): # 최대 4칸 이동할 수 있으니 범위는 4
        ny = y + dir[d][0] * i
        nx = x + dir[d][1] * i
        if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx] != 0: # 상어가 이동할 수 있는 경로만 dfs탐색
            shark = [ny, nx, fish[board[ny][nx]][2]]
            dfs(eat + board[ny][nx], shark, copy.deepcopy(board), copy.deepcopy(fish)) # board, fish는 복사본을 이용


dfs(board_init[0][0], [0,0,fish_init[board_init[0][0]][2]], board_init, fish_init)
print(answer)