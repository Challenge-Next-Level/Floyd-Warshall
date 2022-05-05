import sys


dice = [[-1, 0, -1], [0, 0, 0], [-1, 0, -1], [-1, 0, -1]]


def move_dice(num):
    global dice
    if num == 1:
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = temp
    elif num == 2:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    elif num == 3:
        temp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp
    elif num == 4:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp


n, m, x, y, k = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
command = list(map(int, sys.stdin.readline().split()))

direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]


for com in command:
    ny, nx = y + direction[com - 1][0], x + direction[com - 1][1]
    if not (0 <= ny < n and 0 <= nx < m):
        continue
    move_dice(com)
    if board[ny][nx] != 0:
        dice[1][1] = board[ny][nx]
        board[ny][nx] = 0
    else:
        board[ny][nx] = dice[1][1]
    y, x = ny, nx
    print(str(dice[3][1]))


