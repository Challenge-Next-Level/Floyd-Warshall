import sys
from collections import defaultdict

input = sys.stdin.readline

r, c, k = map(int, input().split())
board = list()
for _ in range(3):
    board.append(list(map(int, input().split())))


def rotate(target_board):
    rotated_board = list()
    for _x in range(len(target_board[0])):
        x_board = list()
        for _y in range(len(target_board)):
            x_board.append(target_board[_y][_x])
        rotated_board.append(x_board)

    return rotated_board


# R 연산 : 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산 : 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
def operator():
    global board
    # 행의 개수 < 열의 개수 -> C 연산
    rotated = False
    if len(board) < len(board[0]):
        board = rotate(board)
        rotated = True

    new_board = [[] for _ in range(len(board))]
    max_len = 0
    for _y in range(len(board)):
        new_y_board = list()
        cnt_dict = defaultdict(int)
        for _x in range(len(board[0])):
            if board[_y][_x] != 0:
                cnt_dict[board[_y][_x]] += 1

        for key, value in cnt_dict.items():
            new_y_board.append([key, value])

        new_y_board.sort(key=lambda x: [x[1], x[0]])

        for new_y in new_y_board:
            new_board[_y].extend(new_y)
        max_len = max(max_len, len(new_board[_y]))

    for _y in range(len(new_board)):
        new_board[_y].extend([0] * (max_len - len(new_board[_y])))
        if len(new_board[_y]) > 100:
            new_board[_y] = new_board[_y][:100]

    if rotated:
        new_board = rotate(new_board)
    board = new_board


sec = 0
while True:
    if sec == 101:
        print(-1)
        exit()
    if len(board) >= r and len(board[0]) >= c:
        if board[r - 1][c - 1] == k:
            print(sec)
            exit()
    operator()
    sec += 1
