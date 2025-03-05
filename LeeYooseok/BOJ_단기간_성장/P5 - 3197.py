import sys

input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
board = list()
bird_loc_list = list()
for _y in range(R):
    x_board = list(input())
    for _x in range(C):
        if x_board[_x] == 'L':
            bird_loc_list.append([_x, _y])
    board.append(x_board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count_of_ice = 1e9
visited = [[-1 for _ in range(C)] for _ in range(R)]

queue = deque([[0, bird_loc_list[0][0], bird_loc_list[0][1]]])
visited[bird_loc_list[0][1]][bird_loc_list[0][0]] = 0

while queue:
    now_count_of_ice, now_x, now_y = queue.popleft()

    if now_x == bird_loc_list[1][0] and now_y == bird_loc_list[1][1]:
        count_of_ice = min(now_count_of_ice, count_of_ice)
        continue

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < C) or not(0 <= new_y < R):
            continue

        new_count_of_ice = now_count_of_ice
        if board[new_y][new_x] == 'X':
            new_count_of_ice += 1

        if 0 <= visited[new_y][new_x] <= new_count_of_ice:
            continue

        visited[new_y][new_x] = new_count_of_ice
        queue.append([new_count_of_ice, new_x, new_y])

print((count_of_ice + 1) // 2)


