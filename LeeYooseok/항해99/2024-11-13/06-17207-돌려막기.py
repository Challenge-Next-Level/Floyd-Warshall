import sys

input = sys.stdin.readline

A_board = [list(map(int, input().split())) for _ in range(5)]
B_board = [list(map(int, input().split())) for _ in range(5)]

work_size = []
for _y in range(5):
    now_work_size = 0
    for _x in range(5):
        now_value = 0
        for i in range(5):
            now_value += (A_board[_y][i] * B_board[i][_x])

        now_work_size += now_value
    work_size.append(now_work_size)

name_list = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
min_work_size = min(work_size)
answer = list()
for i in range(4, -1, -1):
    if work_size[i] == min_work_size:
        answer.append(i)

print(name_list[answer[0]])