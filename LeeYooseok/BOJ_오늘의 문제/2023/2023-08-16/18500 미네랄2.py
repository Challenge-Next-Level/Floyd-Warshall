# 왼쪽부터 막대를 날린다.

from collections import deque

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]


N = int(input())
stick_list = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 막대 던지기
def throw(h, i):
    h = R - h
    # 왼쪽에서 던짐
    if i % 2 == 0:
        for _c in range(C):
            if board[h][_c] == 'x':
                board[h][_c] = '.'
                return h, _c
    # 오른쪽에서 던짐
    elif i % 2 == 1:
        for _c in range(C - 1, -1, -1):
            if board[h][_c] == 'x':
                board[h][_c] = '.'
                return h, _c
    return h, -1

# 떨어질 클러스터인지 확인
def check(c_y, c_x):
    # min_y 가 0 보다 크면 떨어질 클러스터
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dq = deque()
    dq.append([c_y, c_x])
    visited[c_y][c_x] = 1
    block = list()
    chk = True

    # 해당 클러스터 중 가장 아래쪽에 위치한 블럭
    lowest_block = list()

    while dq:
        now_y, now_x = dq.popleft()
        block.append([now_y, now_x])
        if now_y == R - 1:
            chk = False
            break

        if now_y < R - 1:
            if board[now_y + 1][now_x] == '.':
                lowest_block.append([now_y, now_x])

        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if not(0 <= new_y < R) or not(0 <= new_x < C):
                continue

            if visited[new_y][new_x] != 0:
                continue

            if board[new_y][new_x] == '.':
                continue

            visited[new_y][new_x] = 1

            dq.append([new_y, new_x])
    if not chk:
        return chk, block, 0

    fall_depth = 1e9
    for block_y, block_x in lowest_block:
        now_depth = 0
        for _y in range(block_y + 1, R):
            if board[_y][block_x] == 'x' and visited[_y][block_x] != 1:
                break
            now_depth += 1
        fall_depth = min(fall_depth, now_depth)

    return chk, block, fall_depth

# 보드판 조정
def fall(fall_block, fall_depth):
    fall_block.sort(reverse=True)

    for block_y, block_x in fall_block:
        board[block_y][block_x] = '.'
        board[block_y + fall_depth][block_x] = 'x'


def edit_board(_y, _x):
    # 부서진 곳 상, 하, 좌, 우 -> 내려갈 클러스터 확인
    for i in range(4):
        c_y, c_x = _y + dy[i], _x + dx[i]

        if not(0 <= c_y < R) or not(0 <= c_x < C):
            continue

        if board[c_y][c_x] == 'x':
            fall_chk, fall_block, fall_depth = check(c_y, c_x)
            if fall_chk:
                fall(fall_block, fall_depth)


for i in range(N):
    break_y, break_x = throw(stick_list[i], i)

    if break_x != -1:
        edit_board(break_y, break_x)

for b in board:
    for _x in b:
        print(_x, end="")
    print()