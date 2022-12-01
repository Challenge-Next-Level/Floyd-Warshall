import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_board = [list(map(int, input().split())) for _ in range(N)]

prefix_sum_board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _y in range(N):
    for _x in range(N):
        prefix_sum_board[_y + 1][_x + 1] = prefix_sum_board[_y][_x + 1] + prefix_sum_board[_y + 1][_x] - prefix_sum_board[_y][_x] + num_board[_y][_x]

for _ in range(M):
    y_1, x_1, y_2, x_2 = map(int, input().split())

    answer = prefix_sum_board[y_2][x_2] - (prefix_sum_board[y_2][x_1 - 1] + prefix_sum_board[y_1 - 1][x_2]) + prefix_sum_board[y_1 - 1][x_1 - 1]

    print(answer)