import sys

input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
board = list()

start = (0, 0)
fire_list = list()

for _y in range(R):
    x_board = list(input())
    for _x in range(C):
        if x_board[_x] == 'J':
            start = (_x, _y)
            x_board[_x] = '.'
        if x_board[_x] == 'F':
            fire_list.append([_x, _y])

    board.append(x_board)

visited = [[False for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([start[0], start[1], 0])

while queue:
    now_x, now_y, move_cnt = queue.popleft()

    # 종료 조건
    if (now_x == 0 or now_x == C - 1 or now_y == 0 or now_y == R - 1) and board[now_y][now_x] != 'F':
        print(move_cnt + 1)
        exit()

    # 이동
    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < C) or not(0 <= new_y < R):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] != ".":
            continue

        visited[new_y][new_x] = True
        queue.append([new_x, new_y, move_cnt + 1])

    # 불 옮기기
    if queue and queue[0][2] > move_cnt:
        # 불 옮기기
        new_fire_list = set()
        for fire_x, fire_y in fire_list:
            for i in range(4):
                new_fire_x, new_fire_y = fire_x + dx[i], fire_y + dy[i]

                if not (0 <= new_fire_x < C) or not (0 <= new_fire_y < R):
                    continue

                if board[new_fire_y][new_fire_x] != ".":
                    continue

                board[new_fire_y][new_fire_x] = "F"
                new_fire_list.add((new_fire_x, new_fire_y))
        fire_list = list(new_fire_list)

print("IMPOSSIBLE")