import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = list()
start_x, start_y = 0, 0
building_cnt = 0
for _y in range(N):
    x_board = list(input().rstrip())
    for _x in range(M):
        if x_board[_x] == "@":
            start_x, start_y = _x, _y
            x_board[_x] = "."
        elif x_board[_x] == "*" or x_board[_x] == "#":
            building_cnt += 1
    board.append(x_board)

hit_count_board = [[0 for _ in range(M)] for _ in range(N)]
disaster_loc_list = [[start_x, start_y, 2]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

destroyed_building_count = 0

while disaster_loc_list:
    next_disaster_loc_list = list()
    while disaster_loc_list:
        now_x, now_y, power = disaster_loc_list.pop()

        for i in range(4):
            for p in range(1, power + 1):
                new_x, new_y = now_x + p * dx[i], now_y + p * dy[i]

                if not (0 <= new_x < M) or not (0 <= new_y < N):
                    continue

                if board[new_y][new_x] == "|":
                    break

                if board[new_y][new_x] == "*":
                    hit_count_board[new_y][new_x] += 1

                    if hit_count_board[new_y][new_x] == 1:
                        next_disaster_loc_list.append([new_x, new_y, 1])
                        destroyed_building_count += 1
                        board[new_y][new_x] = "."

                if board[new_y][new_x] == "#":
                    hit_count_board[new_y][new_x] += 1

                    if hit_count_board[new_y][new_x] == 2:
                        next_disaster_loc_list.append([new_x, new_y, 1])
                        destroyed_building_count += 1
                        board[new_y][new_x] = "."
    disaster_loc_list = next_disaster_loc_list[:]

print(destroyed_building_count, building_cnt - destroyed_building_count)