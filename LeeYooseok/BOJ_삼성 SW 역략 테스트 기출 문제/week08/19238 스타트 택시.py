import sys
from collections import deque

input = sys.stdin.readline

# N x N 크키 board, M 명의 승객, F - 초기 연료량
N, M, F = map(int, input().split())

# 1 - 벽, 0 - 빈칸
board = [list(map(int, input().split())) for _ in range(N)]

# 운전을 시작하는 행, 열 번호
y, x = map(int, input().split())
y, x = y - 1, x - 1

# 승객의 출발지 행, 열 번호, 목적지 행, 열 번호
cus_start = list()
cus_end = list()
for _ in range(M):
    s_y, s_x, e_y, e_x = map(int, input().split())

    cus_start.append([s_y - 1, s_x - 1])
    cus_end.append([e_y - 1, e_x - 1])


# 북, 서, 남, 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 모든 승객을 다 배송 시킬때까지 반복 그리고 연료가 0 이상 있을 때까지
while cus_end and F >= 0:
    # 가장 가까운 승객에게 이동
    queue = deque()
    queue.append([y, x, 0])
    visited = [item[:] for item in board]
    visited[y][x] = 1

    cus_flag = False
    now_cus = [sys.maxsize, sys.maxsize, sys.maxsize]

    while queue:
        now_y, now_x, cnt = queue.popleft()

        if [now_y, now_x] in cus_start:
            cus_flag = True
            if cnt < now_cus[0]:
                now_cus = [cnt, now_y, now_x]
            elif cnt == now_cus[0]:
                if now_y < now_cus[1]:
                    now_cus = [cnt, now_y, now_x]
                elif now_y == now_cus[1]:
                    if now_x < now_cus[2]:
                        now_cus = [cnt, now_y, now_x]

        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if not(0 <= new_x < N) or not(0 <= new_y < N):
                continue

            if visited[new_y][new_x] == 1:
                continue

            if cnt + 1 > now_cus[0]:
                continue

            visited[new_y][new_x] = 1
            queue.append([new_y, new_x, cnt + 1])
    if not cus_flag:
        print(-1)
        exit()

    if now_cus[0] > F:
        F -= now_cus[0]
        break
    else:
        F -= now_cus[0]
    y, x = now_cus[1], now_cus[2]
    idx = cus_start.index([y, x])

    queue = deque()
    queue.append([y, x, 0])
    visited = [item[:] for item in board]

    flag = False
    while queue:
        now_y, now_x, cnt = queue.popleft()
        if [now_y, now_x] == cus_end[idx]:
            flag = True
            # 연료 확인
            if cnt > F:
                F -= cnt
            else:
                F += cnt
                cus_start.pop(idx)
                cus_end.pop(idx)
                y, x = now_y, now_x
            break

        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if not(0 <= new_y < N) or not(0 <= new_x < N):
                continue

            if visited[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = 1
            queue.append([new_y, new_x, cnt + 1])
    if not flag:
        print(-1)
        exit()

if F < 0:
    print(-1)
else:
    print(F)


