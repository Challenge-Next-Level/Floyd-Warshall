import sys

input = sys.stdin.readline

N = int(input())

board = [input() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

heart_y, heart_x = 0, 0
heart_find = False
for _y in range(N):
    for _x in range(N):
        if not board[_y][_x] == '*':
            continue

        count_body = 0

        for i in range(4):
            n_x, n_y = _x + dx[i], _y + dy[i]

            if not(0 <= n_x < N) or not(0 <= n_y < N):
                continue

            if board[n_y][n_x] == '*':
                count_body += 1

        if count_body == 4:
            heart_y, heart_x = _y, _x
            heart_find = True
            break
    if heart_find:
        break

print(heart_y + 1, heart_x + 1)

# 왼쪽 팔
left_arm_size = 0
x, y = heart_x, heart_y
while True:
    x = x + dx[0]
    if not (0 <= x < N):
        break
    if board[y][x] != "*":
        break

    left_arm_size += 1

# 오른쪽 팔
right_arm_size = 0
x, y = heart_x, heart_y
while True:
    x = x + dx[1]
    if not (0 <= x < N):
        break

    if board[y][x] != "*":
        break

    right_arm_size += 1

waist_size = 0
x, y = heart_x, heart_y
while True:
    y = y + dy[3]
    if not (0 <= y < N):
        break

    if board[y][x] != "*":
        break

    waist_size += 1

waist_end_y = y

left_leg_size = 0
x, y = heart_x - 1, waist_end_y - 1
while True:
    y = y + dy[3]

    if not (0 <= y < N):
        break
    if board[y][x] != "*":
        break

    left_leg_size += 1

right_leg_size = 0
x, y = heart_x + 1, waist_end_y - 1
while True:
    y = y + dy[3]
    if not (0 <= y < N):
        break

    if board[y][x] != "*":
        break

    right_leg_size += 1

print(left_arm_size, right_arm_size, waist_size, left_leg_size, right_leg_size)