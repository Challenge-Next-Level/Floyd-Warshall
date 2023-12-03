from copy import deepcopy

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
operation_list = list(map(int, input().split()))

# 입력받은 보드를 4 구간으로 나누기
divided_board = [[[0 for _ in range(M // 2)] for _ in range(N // 2)] for _ in range(4)]

# 0, 0
for _y in range(N // 2):
    for _x in range(M // 2):
        divided_board[0][_y][_x] = board[_y][_x]

# 0, 1
for _y in range(N // 2):
    for _x in range(M // 2, M):
        divided_board[1][_y][_x - M // 2] = board[_y][_x]

# 1, 0
for _y in range(N // 2, N):
    for _x in range(M // 2):
        divided_board[2][_y - N // 2][_x] = board[_y][_x]

# 1, 1
for _y in range(N // 2, N):
    for _x in range(M // 2, M):
        divided_board[3][_y - N // 2][_x - M // 2] = board[_y][_x]

# 전체 배열을 돌리지 않고, 단순한 형태를 돌려서 결과만 복원하기
sample_board = [[0, 1], [2, 3]]

# 상하 반전
up_down_revision = False

# 좌우 반전
left_right_revision = False

# 회전 수
rotate_cnt = 0


# 각 배열 회전 명령어
# 1 - 배열을 상하 반전시키는 연산
def operation_1():
    global sample_board, up_down_revision, left_right_revision
    # 배열이 90도, 270도 회전되어 있는채로 상하 반전 -> 좌우 반전
    if rotate_cnt % 2 == 0:
        up_down_revision = not up_down_revision
    else:
        left_right_revision = not left_right_revision

    sample_board[0], sample_board[1] = sample_board[1], sample_board[0]


# 2 - 배열을 좌우 반전시키는 연산
def operation_2():
    global sample_board, up_down_revision, left_right_revision
    # 배열이 90도, 270도 회전되어 있는채로 좌우 반전 -> 상하 반전
    if rotate_cnt % 2 == 0:
        left_right_revision = not left_right_revision
    else:
        up_down_revision = not up_down_revision

    sample_board[0][1], sample_board[0][0] = sample_board[0][0], sample_board[0][1]
    sample_board[1][1], sample_board[1][0] = sample_board[1][0], sample_board[1][1]


# 3 - 오른쪽으로 90도 회전시키는 연산
def operation_3():
    global rotate_cnt
    rotate_cnt = (rotate_cnt + 1) % 4

    # 보드를 오른쪽으로 90도 회전
    operation_5()


# 4 - 왼쪽으로 90도 회전시키는 연산
def operation_4():
    global rotate_cnt
    rotate_cnt = (rotate_cnt - 1) % 4

    # 보드를 왼쪽으로 90도 회전
    operation_6()


# 5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다.
# 5 - 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산 (오른쪽 90도)
def operation_5():
    global sample_board

    rotated_sample_board = [[0, 0], [0, 0]]

    rotated_sample_board[0][0] = sample_board[1][0]
    rotated_sample_board[0][1] = sample_board[0][0]
    rotated_sample_board[1][0] = sample_board[1][1]
    rotated_sample_board[1][1] = sample_board[0][1]

    sample_board = rotated_sample_board.copy()


# 6 - 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산 (왼쪽 90도)
def operation_6():
    global sample_board

    rotated_sample_board = [[0, 0], [0, 0]]

    rotated_sample_board[0][0] = sample_board[0][1]
    rotated_sample_board[0][1] = sample_board[1][1]
    rotated_sample_board[1][0] = sample_board[0][0]
    rotated_sample_board[1][1] = sample_board[1][0]

    sample_board = rotated_sample_board.copy()


func_list = [0, operation_1, operation_2, operation_3, operation_4, operation_5, operation_6]

# 입력받은 명령어 수행
for operation in operation_list:
    func_list[operation]()

# 정답 복원
# 상하 반전
if up_down_revision:
    for i in range(4):
        divided_board[i].reverse()

# 좌우 반전
if left_right_revision:
    for i in range(4):
        for _y in range(N // 2):
            divided_board[i][_y].reverse()


# 배열 회전 - 오른쪽으로 90도
def rotate_board(_board):
    rotated_board = [[0 for _ in range(len(_board))] for _ in range(len(_board[0]))]

    for _y in range(len(_board)):
        for _x in range(len(_board[0])):
            rotated_board[_x][_y] = _board[len(_board) - _y - 1][_x]

    return rotated_board


for _ in range(rotate_cnt):
    for i in range(4):
        divided_board[i] = rotate_board(divided_board[i])

answer_board = []

answer_board.extend(deepcopy(divided_board[sample_board[0][0]]))
for _y in range(N // 2):
    answer_board[_y].extend(divided_board[sample_board[0][1]][_y])

answer_board.extend(deepcopy(divided_board[sample_board[1][0]]))
for _y in range(N // 2, N):
    answer_board[_y].extend(divided_board[sample_board[1][1]][_y - (N // 2)])

for y_board in answer_board:
    print(*y_board)