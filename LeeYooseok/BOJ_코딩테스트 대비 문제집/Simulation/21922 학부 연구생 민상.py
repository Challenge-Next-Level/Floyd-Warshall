import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = list()
loc_AC_list = list()
for n in range(N):
    x_board = list(map(int, input().split()))
    for m in range(M):
        if x_board[m] == 9:
            loc_AC = [m, n]
            loc_AC_list.append(loc_AC)
    board.append(x_board)
if len(loc_AC_list) == 0:
    print(0)
    exit()

# 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]

answer = set()

que = deque()
for loc_AC in loc_AC_list:
    for i in range(4):
        que.append([loc_AC[0], loc_AC[1], i])
        visited[loc_AC[1]][loc_AC[0]][i] = 1
while que:
    now_x, now_y, now_d = que.popleft()
    answer.add((now_x, now_y))

    new_x, new_y = now_x + dx[now_d], now_y + dy[now_d]
    if not(0 <= new_x < M) or not(0 <= new_y < N):
        continue
    # 방향 전환
    thing = board[new_y][new_x]
    new_d = now_d
    if thing == 1:
        if now_d == 0:
            new_d = 1
        elif now_d == 1:
            new_d = 0
    elif thing == 2:
        if now_d == 2:
            new_d = 3
        elif now_d == 3:
            new_d = 2
    elif thing == 3:
        if now_d == 0:
            new_d = 3
        elif now_d == 1:
            new_d = 2
        elif now_d == 2:
            new_d = 1
        elif now_d == 3:
            new_d = 0
    elif thing == 4:
        if now_d == 0:
            new_d = 2
        elif now_d == 1:
            new_d = 3
        elif now_d == 2:
            new_d = 0
        elif now_d == 3:
            new_d = 1

    if visited[new_y][new_x][new_d] == 0:
        que.append([new_x, new_y, new_d])
        visited[new_y][new_x][new_d] = 1

print(len(answer))


