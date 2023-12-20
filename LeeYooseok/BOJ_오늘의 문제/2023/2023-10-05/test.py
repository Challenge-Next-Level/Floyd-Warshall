k = int(input())

board = [list(input()) for _ in range(4 * k)]

now_x, now_y = map(int, input().split())

rot_x, rot_y = (now_x // 4) * 4, (now_y // 4) * 4
print(rot_x, rot_y)

temp_board = [item[:] for item in board]

# rotate 90
for r_x in range(4):
    for r_y in range(4):
        temp_board[r_x + rot_y][4 - 1 - r_y + rot_x] = board[r_y + rot_y][r_x + rot_x]

# rotate 180
# for r_x in range(4):
#     for r_y in range(4):
#         temp_board[4 - 1 - r_y + rot_y][4 - 1 - r_x + rot_x] = board[r_y + rot_y][r_x + rot_x]

# rotate 270
# for r_x in range(4):
#     for r_y in range(4):
#         temp_board[4 - 1 - r_x + rot_y][r_y + rot_x] = board[r_y + rot_y][r_x + rot_x]

for b in temp_board:
    print(*b)