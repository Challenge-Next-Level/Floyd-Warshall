R, S = map(int, input().split())

board = [list(input()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    now_drop_h = 0
    flag = True
    for drop_y in range(y + 1, R):
        if board[drop_y][x] == 'X':
            flag = False
            break

        if board[drop_y][x] == '#':
            break
        now_drop_h += 1

    if flag:
        return now_drop_h
    else:
        return 1e9


drop_h = 1e9

for _y in range(R):
    for _x in range(S):
        if board[_y][_x] == 'X':
            drop_h = min(drop_h, check(_x, _y))

for _y in range(R - 1, -1, -1):
    for _x in range(S):
        if board[_y][_x] == 'X':
            board[_y + drop_h][_x] = 'X'
            board[_y][_x] = '.'

for b in board:
    for _x in b:
        print(_x, end = "")
    print()
