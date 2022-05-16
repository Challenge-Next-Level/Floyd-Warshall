import sys

n, m, h = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = 1

possible = []
for y in range(h):
    for x in range(n - 1):
        if board[y][x] == 1:
            continue
        if x - 1 >= 0 and board[y][x - 1] == 1:
            continue
        if board[y][x + 1] != 1:
            possible.append([y, x])
length = len(possible)


def is_answer():
    for x in range(n):
        node = [0, x]
        if board[0][x] == 1:
            node[1] += 1
        elif board[0][x - 1] == 1:
            node[1] -= 1
        for _ in range(1, h):
            node[0] += 1
            if board[node[0]][node[1]] == 1:
                node[1] += 1
            elif board[node[0]][node[1] - 1] == 1:
                node[1] -= 1
        if node[1] != x:
            return False
    return True


def result():
    if m == 0:
        return 0
    # 다리 1개 일 때
    for p in possible:
        ny, nx = p[0], p[1]
        board[ny][nx] = 1
        if is_answer():
            return 1
        board[ny][nx] = 0
    # 다리 2개 일 때
    for i in range(length - 1):
        iy, ix = possible[i][0], possible[i][1]
        board[iy][ix] = 1
        for j in range(i + 1, length):
            jy, jx = possible[j][0], possible[j][1]
            if board[jy][jx] == 1 or (jx - 1 >= 0 and board[jy][jx - 1] == 1) or board[jy][jx + 1] == 1:
                continue
            board[jy][jx] = 1
            if is_answer():
                return 2
            board[jy][jx] = 0
        board[iy][ix] = 0
    # 다리 3개 일 때
    for i in range(length - 2):
        iy, ix = possible[i][0], possible[i][1]
        board[iy][ix] = 1
        for j in range(i + 1, length - 1):
            jy, jx = possible[j][0], possible[j][1]
            if board[jy][jx] == 1 or (jx - 1 >= 0 and board[jy][jx - 1] == 1) or board[jy][jx + 1] == 1:
                continue
            board[jy][jx] = 1
            for k in range(j + 1, length):
                ky, kx = possible[k][0], possible[k][1]
                if board[ky][kx] == 1 or (kx - 1 >= 0 and board[ky][kx - 1] == 1) or board[ky][kx + 1] == 1:
                    continue
                board[ky][kx] = 1
                if is_answer():
                    return 3
                board[ky][kx] = 0
            board[jy][jx] = 0
        board[iy][ix] = 0
    return -1


print(result())