board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]


def check(_x, _y):
    global board

    turn = board[_y][_x]

    for i in range(4):
        # 범위 안인지 확인
        if _y + dy[i] * 4 >= 19 or _x + dx[i] * 4 >= 19:
            continue
        chk = True
        for n in range(1, 5):
            if board[_y + dy[i] * n][_x + dx[i] * n] != turn:
                chk = False

        if chk:
            # 6목인지 확인
            if _y + dy[i] * 5 < 19 and _x + dx[i] * 5 < 19:
                if board[_y + dy[i] * 5][_x + dx[i] * 5] == turn:
                    chk = False

            if i != 3:
                if _y - dy[i] >= 0 and _x - dx[i] >= 0:
                    if board[_y - dy[i]][_x - dx[i]] == turn:
                        chk = False
            else:
                if _y - dy[i] < 19 and _x - dx[i] >= 0:
                    if board[_y - dy[i]][_x - dx[i]] == turn:
                        chk = False
        if chk:
            return True
    return False


for _y in range(19):
    for _x in range(19):
        if board[_y][_x] != 0:
            if check(_x, _y):
                print(board[_y][_x])
                print(_y + 1, _x + 1)
                exit()
print(0)
