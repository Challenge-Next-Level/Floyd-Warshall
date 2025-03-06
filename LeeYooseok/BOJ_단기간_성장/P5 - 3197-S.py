import sys

input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

swan_queue, swan_temp_queue, water_queue, water_temp_queue = deque(), deque(), deque(), deque()

R, C = map(int, input().split())

swan_visited = [[False for _ in range(C)] for _ in range(R)]
water_visited = [[False for _ in range(C)] for _ in range(R)]

board = list()
swan_loc_list = list()
for _y in range(R):
    x_board = list(input().rstrip())
    for _x in range(C):
        if x_board[_x] == 'L':
            swan_loc_list.append([_x, _y])
            water_queue.append([_x, _y])
        elif x_board[_x] == '.':
            water_visited[_y][_x] = True
            water_queue.append([_x, _y])
    board.append(x_board)

swan_1_x, swan_1_y = swan_loc_list[0]
swan_2_x, swan_2_y = swan_loc_list[1]
swan_queue.append([swan_1_x, swan_1_y])
swan_visited[swan_1_y][swan_1_x] = True
board[swan_1_y][swan_1_x] = '.'
board[swan_2_y][swan_2_x] = '.'

answer = 0


def water_bfs():
    while water_queue:
        now_x, now_y = water_queue.popleft()

        # 빙판 녺은것 board 에 표시
        if board[now_y][now_x] == 'X':
            board[now_y][now_x] = '.'

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < C) or not (0 <= new_y < R):
                continue

            if water_visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == 'X':
                # 현재 step 에서 녺는 빙판
                water_temp_queue.append([new_x, new_y])
            else:
                water_queue.append([new_x, new_y])
            water_visited[new_y][new_x] = True


def swan_bfs():
    while swan_queue:
        now_x, now_y = swan_queue.popleft()

        if now_x == swan_2_x and now_y == swan_2_y:
            return True

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < C) or not (0 <= new_y < R):
                continue

            if swan_visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == ".":
                swan_queue.append([new_x, new_y])
            else:
                swan_temp_queue.append([new_x, new_y])

            swan_visited[new_y][new_x] = True
    return False


while True:

    water_bfs()
    if swan_bfs():
        print(answer)
        break
    swan_queue, water_queue = swan_temp_queue, water_temp_queue
    swan_temp_queue, water_temp_queue = deque(), deque()
    answer += 1
