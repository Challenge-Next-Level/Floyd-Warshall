import sys

input = sys.stdin.readline

from collections import defaultdict

number_loc_dict = defaultdict(list)

for _y in range(5):
    x_board = list(map(int, input().split()))
    for _x in range(5):
        number = x_board[_x]
        number_loc_dict[number] = [_x, _y]

bingo_board = [[0 for _ in range(5)] for _ in range(5)]

count_bingo = 0
center_bingo = [False, False]


def check_bingo(now_x, now_y):
    global count_bingo
    # 가로
    x_completed = True
    for _x in range(5):
        if bingo_board[now_y][_x] == 0:
            x_completed = False
            break
    if x_completed:
        count_bingo += 1
    # 세로
    y_completed = True
    for _y in range(5):
        if bingo_board[_y][now_x] == 0:
            y_completed = False
    if y_completed:
        count_bingo += 1
    # 대각선
    if now_x == now_y and not center_bingo[0]:
        axis_completed = True
        for i in range(5):
            if bingo_board[i][i] == 0:
                axis_completed = False
                break
        if axis_completed:
            center_bingo[0] = True
            count_bingo += 1
    if now_x == (4 - now_y) and not center_bingo[1]:
        axis_completed = True
        for i in range(5):
            if bingo_board[i][4 - i] == 0:
                axis_completed = False
                break
        if axis_completed:
            center_bingo[1] = True
            count_bingo += 1


number_input_list = list()
for _ in range(5):
    number_input_list.extend(list(map(int, input().split())))

for i in range(25):
    number = number_input_list[i]

    number_x, number_y = number_loc_dict[number]
    bingo_board[number_y][number_x] = 1

    check_bingo(number_x, number_y)
    if count_bingo >= 3:
        print(i + 1)
        exit()
