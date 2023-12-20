# 전개도 9 * 12
cube = [[0] * 9 for _ in range(12)]

for i in range(3, 6):
    # white
    for j in range(0, 3):
        cube[j][i] = 'w'
    # red
    for j in range(3, 6):
        cube[j][i] = 'r'
    # yellow
    for j in range(6, 9):
        cube[j][i] = 'y'
    # orange
    for j in range(9, 12):
        cube[j][i] = 'o'

# green
for i in range(0, 3):
    for j in range(3, 6):
        cube[j][i] = 'g'

# blue
for i in range(6, 9):
    for j in range(3, 6):
        cube[j][i] = 'b'

n = int(input())


def rotate(self_board, d):
    new_board = [[0] * 3 for _ in range(3)]
    if d == '+':
        new_board[0][2] = self_board[0][0]
        new_board[1][2] = self_board[0][1]
        new_board[2][2] = self_board[0][2]

        new_board[0][1] = self_board[1][0]
        new_board[1][1] = self_board[1][1]
        new_board[2][1] = self_board[1][2]

        new_board[0][0] = self_board[2][0]
        new_board[1][0] = self_board[2][1]
        new_board[2][0] = self_board[2][2]
    else:
        new_board[0][0] = self_board[0][2]
        new_board[1][0] = self_board[0][1]
        new_board[2][0] = self_board[0][0]

        new_board[0][1] = self_board[1][2]
        new_board[1][1] = self_board[1][1]
        new_board[2][1] = self_board[1][0]

        new_board[0][2] = self_board[2][2]
        new_board[1][2] = self_board[2][1]
        new_board[2][2] = self_board[2][0]

    return new_board


def check(o):
    # 방향, 시계 방향
    d, c = o[0], o[1]

    # 윗면 회전
    if d == 'U':
        if c == '+':
            temp = temp_cube[3][0:3]
            temp_cube[3][0:6] = temp_cube[3][3:9]
            temp_cube[3][6:9] = temp_cube[11][5:2:-1]
            temp_cube[11][3:6] = temp[::-1]

        else:
            temp = temp_cube[3][6:9]
            temp_cube[3][3:9] = temp_cube[3][0:6]
            temp_cube[3][0:3] = temp_cube[11][5:2:-1]
            temp_cube[11][3:6] = temp[::-1]

        # 자기 자신 회전
        _self = [temp_cube[0][3:6], temp_cube[1][3:6], temp_cube[2][3:6]]
        new_self = rotate(_self, c)
        for i in range(3):
            for j in range(3, 6):
                temp_cube[i][j] = new_self[i][j - 3]
    # 아랫면 회전
    if d == 'D':
        if c == '+':
            temp = temp_cube[5][6:9]
            temp_cube[5][3:9] = temp_cube[5][0:6]
            temp_cube[5][0:3] = temp_cube[9][5:2:-1]
            temp_cube[9][3:6] = temp[::-1]
        else:
            temp = temp_cube[5][0:3]
            temp_cube[5][0:6] = temp_cube[5][3:9]
            temp_cube[5][6:9] = temp_cube[9][5:2:-1]
            temp_cube[9][3:6] = temp[::-1]

        # 자기 자신 회전
        _self = [temp_cube[6][3:6], temp_cube[7][3:6], temp_cube[8][3:6]]
        new_self = rotate(_self, c)
        for i in range(6, 9):
            for j in range(3, 6):
                temp_cube[i][j] = new_self[i - 6][j - 3]
    # 앞면 회전
    if d == 'F':
        if c == '+':
            temp = temp_cube[2][3:6]
            temp_cube[2][3] = temp_cube[5][2]
            temp_cube[2][4] = temp_cube[4][2]
            temp_cube[2][5] = temp_cube[3][2]

            temp_cube[3][2] = temp_cube[6][3]
            temp_cube[4][2] = temp_cube[6][4]
            temp_cube[5][2] = temp_cube[6][5]

            temp_cube[6][3] = temp_cube[5][6]
            temp_cube[6][4] = temp_cube[4][6]
            temp_cube[6][5] = temp_cube[3][6]

            temp_cube[3][6] = temp[0]
            temp_cube[4][6] = temp[1]
            temp_cube[5][6] = temp[2]
        else:
            temp = temp_cube[2][3:6]
            temp_cube[2][3] = temp_cube[3][6]
            temp_cube[2][4] = temp_cube[4][6]
            temp_cube[2][5] = temp_cube[5][6]

            temp_cube[3][6] = temp_cube[6][5]
            temp_cube[4][6] = temp_cube[6][4]
            temp_cube[5][6] = temp_cube[6][3]

            temp_cube[6][3] = temp_cube[3][2]
            temp_cube[6][4] = temp_cube[4][2]
            temp_cube[6][5] = temp_cube[5][2]

            temp_cube[3][2] = temp[2]
            temp_cube[4][2] = temp[1]
            temp_cube[5][2] = temp[0]

        # 자기 자신 회전
        _self = [temp_cube[3][3:6], temp_cube[4][3:6], temp_cube[5][3:6]]
        new_self = rotate(_self, c)
        for i in range(3, 6):
            for j in range(3, 6):
                temp_cube[i][j] = new_self[i - 3][j - 3]

    # 뒷면 회전
    if d == 'B':
        if c == '+':
            temp = temp_cube[0][3:6]
            temp_cube[0][3] = temp_cube[3][8]
            temp_cube[0][4] = temp_cube[4][8]
            temp_cube[0][5] = temp_cube[5][8]

            temp_cube[3][8] = temp_cube[8][5]
            temp_cube[4][8] = temp_cube[8][4]
            temp_cube[5][8] = temp_cube[8][3]

            temp_cube[8][3] = temp_cube[3][0]
            temp_cube[8][4] = temp_cube[4][0]
            temp_cube[8][5] = temp_cube[5][0]

            temp_cube[3][0] = temp[2]
            temp_cube[4][0] = temp[1]
            temp_cube[5][0] = temp[0]
        else:
            temp = temp_cube[0][3:6]
            temp_cube[0][3] = temp_cube[5][0]
            temp_cube[0][4] = temp_cube[4][0]
            temp_cube[0][5] = temp_cube[3][0]

            temp_cube[3][0] = temp_cube[8][3]
            temp_cube[4][0] = temp_cube[8][4]
            temp_cube[5][0] = temp_cube[8][5]

            temp_cube[8][3] = temp_cube[5][8]
            temp_cube[8][4] = temp_cube[4][8]
            temp_cube[8][5] = temp_cube[3][8]

            temp_cube[3][8] = temp[0]
            temp_cube[4][8] = temp[1]
            temp_cube[5][8] = temp[2]
        # 자기 자신 회전
        _self = [temp_cube[9][3:6], temp_cube[10][3:6], temp_cube[11][3:6]]
        new_self = rotate(_self, c)
        for i in range(9, 12):
            for j in range(3, 6):
                temp_cube[i][j] = new_self[i - 9][j - 3]

    # 왼쪽면 회전
    if d == 'L':
        if c == '+':
            temp = [temp_cube[9][3], temp_cube[10][3], temp_cube[11][3]]

            for l in range(8, -1, -1):
                temp_cube[l + 3][3] = temp_cube[l][3]

            for l in range(3):
                temp_cube[l][3] = temp[l]
        else:
            temp = [temp_cube[0][3], temp_cube[1][3], temp_cube[2][3]]

            for l in range(0, 9):
                temp_cube[l][3] = temp_cube[l + 3][3]

            for l in range(3):
                temp_cube[l + 9][3] = temp[l]

        # 자기 자신 회전
        _self = [temp_cube[3][0:3], temp_cube[4][0:3], temp_cube[5][0:3]]
        new_self = rotate(_self, c)
        for i in range(3, 6):
            for j in range(3):
                temp_cube[i][j] = new_self[i - 3][j]

    # 오른쪽 면 회전
    if d == 'R':
        if c == '+':
            temp = [temp_cube[0][5], temp_cube[1][5], temp_cube[2][5]]

            for l in range(0, 9):
                temp_cube[l][5] = temp_cube[l + 3][5]

            for l in range(3):
                temp_cube[l + 9][5] = temp[l]
        else:
            temp = [temp_cube[9][5], temp_cube[10][5], temp_cube[11][5]]

            for l in range(8, -1, -1):
                temp_cube[l + 3][5] = temp_cube[l][5]

            for l in range(3):
                temp_cube[l][5] = temp[l]

        # 자기 자신 회전
        _self = [temp_cube[3][6:9], temp_cube[4][6:9], temp_cube[5][6:9]]
        new_self = rotate(_self, c)
        for i in range(3, 6):
            for j in range(6, 9):
                temp_cube[i][j] = new_self[i - 3][j - 6]


for _ in range(n):
    num_o = int(input())

    # cube deepcopy
    temp_cube = [c[:] for c in cube]

    operators = list(input().split())

    for o in operators:
        check(o)

    for c in temp_cube[:3]:
        print("".join(c[3:6]))
