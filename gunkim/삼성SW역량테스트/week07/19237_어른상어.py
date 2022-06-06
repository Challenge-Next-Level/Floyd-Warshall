import sys

n, m, k = list(map(int, sys.stdin.readline().split()))
board = [[[] for _ in range(n)] for _ in range(n)]
shark = [[0 for _ in range(3)] for _ in range(m + 1)] # 상어 번호의 [좌표, 살아있는 여부] 저장
for i in range(n):
    loc = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if loc[j] != 0:
            shark[loc[j]] = [i, j, 1]
            board[i][j].append([loc[j], k])
        else:
            board[i][j].append([loc[j], 0])
shark_dir = list(map(int, sys.stdin.readline().split())) # 상어 초기방향
dir_priority = [[] for _ in range(m + 1)]
for i in range(m):
    for j in range(4):
        dir_priority[i + 1].append(list(map(int, sys.stdin.readline().split())))


def d_p_index(num):
    if num == 1:
        return [-1,0]
    elif num == 2:
        return [1,0]
    elif num == 3:
        return [0,-1]
    elif num == 4:
        return [0,1]

time = 0
while True:
    if time > 1000:
        print(-1)
        break

    alive = 0
    for i in range(1, m + 1):
        alive += shark[i][2]
    if alive == 1:
        print(time)
        break

    location = []
    # 상어 이동
    for i in range(1, m + 1): # m마리 상어 이동
        if shark[i][2] == 0:
            continue
        # 현재 방향에서 우선순위
        flag = 0
        y, x = shark[i][:2]
        d = shark_dir[i - 1] - 1
        for a in range(4):
            go_y, go_x = d_p_index(dir_priority[i][d][a])
            ny, nx = y + go_y, x + go_x
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx][0][0] != 0 or [ny, nx, 1] == shark[board[ny][nx][0][0]]: # 냄새, 상어가 있으면 못간다
                    continue
                location.append([ny, nx, i, 100]) # 상어,보드 좌표 갱신 위함 / 100: 빈 곳 이동
                flag = 1
                shark_dir[i - 1] = dir_priority[i][d][a]
                break
        if flag == 1: # 위에서 이동을 성공했다면 continue
            continue
        for a in range(4): # 위에서 이동을 못했다면 자신의 냄새가 있는 곳으로 이동
            go_y, go_x = d_p_index(dir_priority[i][d][a])
            ny, nx = y + go_y, x + go_x
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx][0][0] == i: # 내 냄새라면
                location.append([ny, nx, i, 200]) # 상어,보드 좌표 갱신 위함 / 200: 내 냄새인 곳 이동
                shark_dir[i - 1] = dir_priority[i][d][a]
                break

    for gy, gx, num, l_flag in location: # 실제로 상어 이동시키기
        shark[num] = [gy, gx, 1] # 상어 좌표 갱신
        if l_flag == 100: # 보드에 상어 번호 남기기
            if board[gy][gx][0][0] == 0:
                board[gy][gx][0] = [num, k + 1]
            else:
                board[gy][gx].append([num, k + 1])
        elif l_flag == 200:
            board[gy][gx][0] = [num, k + 1]

    max_shark = float('inf')
    # 상어가 겹쳐있다면
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                for p in range(len(board[i][j])):
                    if board[i][j][p][0] < max_shark:
                        max_shark = board[i][j][p][0] # 최상위 상어 찾기
                for p in range(len(board[i][j])):
                    if board[i][j][p][0] != max_shark:
                        shark[board[i][j][p][0]][2] = 0 # 상어 죽음
                board[i][j] = [[max_shark, k+1]]

    # 냄새 제거
    for i in range(n):
        for j in range(n):
            if board[i][j][0][0] != 0:
                board[i][j][0][1] -= 1
            if board[i][j][0][1] == 0:
                board[i][j][0][0] = 0
    time += 1