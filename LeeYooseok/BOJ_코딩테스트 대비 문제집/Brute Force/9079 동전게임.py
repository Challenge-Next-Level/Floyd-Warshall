import sys

T = int(input())


def check(board):
    pivot = board[0][0]

    for _y in range(3):
        for _x in range(3):
            if board[_y][_x] != pivot:
                return False
    return True


def solve(board, cnt, idx):
    global answer

    # 최종 원하는 결과와 일치하는지 확인
    if check(board):
        answer = min(cnt, answer)
        return

    # 8번 (모든 경우) 시도했다면 불가능
    if idx == 8:
        return

    solve(board, cnt, idx + 1)

    # 한 행을 뒤집음
    if idx < 3:
        for i in range(3):
            board[idx][i] = 0 if board[idx][i] == 1 else 1
        solve(board, cnt + 1, idx + 1)
        for i in range(3):
            board[idx][i] = 0 if board[idx][i] == 1 else 1
    # 한 열을 뒤집음
    elif idx < 6:
        for i in range(3):
            board[i][idx - 3] = 0 if board[i][idx - 3] == 1 else 1
        solve(board, cnt + 1, idx + 1)
        for i in range(3):
            board[i][idx - 3] = 0 if board[i][idx - 3] == 1 else 1
    # 오른쪽 대각선을 뒤집음
    elif idx == 6:
        for i in range(3):
            board[i][i] = 0 if board[i][i] == 1 else 1
        solve(board, cnt + 1, idx + 1)
        for i in range(3):
            board[i][i] = 0 if board[i][i] == 1 else 1
    # 왼쪽 대각선을 뒤집음
    elif idx == 7:
        for i in range(3):
            board[i][2 - i] = 0 if board[i][2 - i] == 1 else 1
        solve(board, cnt + 1, idx + 1)
        for i in range(3):
            board[i][2 - i] = 0 if board[i][2 - i] == 1 else 1


for _ in range(T):
    board = list()
    answer = sys.maxsize

    for _ in range(3):
        board_x = list()
        input_list = list(input().split())
        for t in input_list:
            if t == 'H':
                board_x.append(1)
            else:
                board_x.append(0)
        board.append(board_x)

    solve(board, 0, 0)

    if answer == sys.maxsize:
        print(-1)
    else:
        print(answer)
