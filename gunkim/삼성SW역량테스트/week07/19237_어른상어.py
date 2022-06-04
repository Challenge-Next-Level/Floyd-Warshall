import sys
from collections import deque

n, m, k = list(map(int, sys.stdin.readline().split()))
board = [[[] for _ in range(n)] for _ in range(n)]
shark = [[0 for _ in range(3)] for _ in range(m + 1)] # 상어 번호의 [좌표, 살아있는 여부] 저장
for i in range(n):
    loc = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        board[i][j].append(loc[j])
        if loc[j] != 0:
            shark[loc[j]] = [i, j, 1]
shark_dir = list(map(int, sys.stdin.readline().split())) # 상어 초기방향
dir_priority = [[] for _ in range(m + 1)]
for i in range(m):
    for j in range(4):
        dir_priority[i + 1].append(list(map(int, sys.stdin.readline().split())))

smell = [deque([[-1, -1] for _ in range(k - 1)]) for _ in range(m + 1)]
print(smell)

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

    # 상어 이동
    for i in range(1, m + 1): # m마리 상어 이동
        if shark[i][2] == 0:
            smell[i].append([-1, -1])
            ky, kx = smell[i].popleft()
            if ky != -1 and ([ky, kx] not in smell[i]):
                print("1111111111111111111111")
                board[ky][kx] = [0]
            continue
        # 현재 방향에서 우선순위
        flag = 0
        y, x = shark[i][:2]
        d = shark_dir[i - 1] - 1
        for a in range(4):
            go_y, go_x = d_p_index(dir_priority[i][d][a])
            ny, nx = y + go_y, x + go_x
            print(ny, nx)
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx][0] != 0 and [ny, nx, 1] != shark[board[ny][nx][0]]: # 냄새면 못간다
                    continue
                shark[i] = [ny, nx, 1] # 상어 좌표 갱신
                if board[ny][nx][0] == 0: # 보드에 상어 번호 남기기
                    board[ny][nx][0] = i
                else:
                    board[ny][nx].append(i)
                smell[i].append([y, x]) # 냄새 좌표 덱에 추가
                print("smell", smell)
                ky, kx = smell[i].popleft()
                if ky != -1 and [ky,kx] != [ny,nx]:
                    print("22222222222222222222222222")
                    board[ky][kx] = [0]
                flag = 1
                shark_dir[i - 1] = dir_priority[i][d][a]
                break
        if flag == 1:
            continue
        for a in range(4):
            go_y, go_x = d_p_index(dir_priority[i][d][a])
            ny, nx = y + go_y, x + go_x
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx][0] == i: # 내 냄새라면
                shark[i] = [ny, nx, 1]  # 상어 좌표 갱신
                smell[i].append([y, x])  # 냄새 좌표 덱에 추가
                ky, kx = smell[i].popleft()
                if ky != -1 and [ky,kx] != [ny,nx]:
                    print("333333333333333333333")
                    board[ky][kx] = [0]
                shark_dir[i - 1] = dir_priority[i][d][a]
                break
    # 상어가 겹쳐있다면
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                max_shark = min(board[i][j])
                for k in range(len(board[i][j])):
                    if board[i][j][k] != max_shark:
                        shark[board[i][j][k]][2] = 0
                board[i][j] = [max_shark]
    print(board)
    time += 1

# import sys
#
# input = sys.stdin.readline
# dx = [0, -1, 1, 0, 0]
# dy = [0, 0, 0, -1, 1]
#
# n, m, k = map(int, input().split())
#
# a, shark = [], [[] for _ in range(m)]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     for j in range(n):
#         if a[i][j]:
#             shark[a[i][j]-1].extend([i, j])
#             a[i][j] = [a[i][j], k]
#
# d = list(map(int, input().split()))
# for i in range(m):
#     shark[i].append(d[i])
#
# dir = [[] for _ in range(m)]
# idx = -1
# for i in range(4*m):
#     if i % 4 == 0:
#         idx += 1
#     dir[idx].append(list(map(int, input().split())))
#
# ans = 0
# while True:
#     ans += 1
#     if ans == 1001:
#         print(-1)
#         break
#
#     check = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(m):
#         if shark[i] != 0:
#             x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
#             for j in range(4):
#                 ndir = dir[i][d-1][j]
#                 nx, ny = x + dx[ndir], y + dy[ndir]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if a[nx][ny] == 0:
#                         flag = 1
#                         break
#             if flag == 0:
#                 for j in range(4):
#                     ndir = dir[i][d-1][j]
#                     nx, ny = x + dx[ndir], y + dy[ndir]
#                     if 0 <= nx < n and 0 <= ny < n:
#                         if a[nx][ny][0] == i+1:
#                             break
#
#             if check[nx][ny]:
#                 if check[nx][ny] < i+1:
#                     shark[i] = 0
#                 else:
#                     shark[check[nx][ny]-1] = 0
#             else:
#                 check[nx][ny] = i+1
#                 shark[i] = [nx, ny, ndir]
#
#     for i in range(n):
#         for j in range(n):
#             if a[i][j]:
#                 a[i][j][1] -= 1
#                 if a[i][j][1] == 0:
#                     a[i][j] = 0
#
#     for i in range(m):
#         if shark[i]:
#             x, y = shark[i][0], shark[i][1]
#             a[x][y] = [i+1, k]
#
#     if shark.count(0) == m-1:
#         print(ans)
#         break