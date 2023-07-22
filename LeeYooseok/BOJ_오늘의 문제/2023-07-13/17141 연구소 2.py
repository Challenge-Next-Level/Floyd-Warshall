# BFS

from itertools import combinations
from collections import deque

N, M = map(int, input().split())

board = list()
virus_loc = list()
wall_cnt = 0
for _y in range(N):
    x_board = list(map(int, input().split()))
    for _x in range(N):
        if x_board[_x] == 2:
            virus_loc.append([_y, _x])
            x_board[_x] = 0
        if x_board[_x] == 1:
            wall_cnt += 1
            x_board[_x] = '-'
    board.append(x_board)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 1e9

for virus_list in combinations(virus_loc, M):
    visited = [item[:] for item in board]
    temp_board = [item[:] for item in board]
    que = deque()
    for _y, _x in virus_list:
        visited[_y][_x] = 1
        que.append([_y, _x])

    while que:
        now_y, now_x = que.popleft()
        now_t = temp_board[now_y][now_x]

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < N) or not(0 <= new_y < N):
                continue

            if temp_board[new_y][new_x] == '-':
                continue

            if visited[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = 1
            temp_board[new_y][new_x] = now_t + 1
            que.append([new_y, new_x])

    ok = True
    for x_visited in visited:
        if 0 in x_visited:
            ok = False
            break
    if ok:
        max_cnt = -1
        for x_temp_board in temp_board:
            for x_temp in x_temp_board:
                if x_temp != '-':
                    max_cnt = max(max_cnt, x_temp)

        answer = min(answer, max_cnt)

if answer == 1e9:
    print(-1)
else:
    print(answer)
