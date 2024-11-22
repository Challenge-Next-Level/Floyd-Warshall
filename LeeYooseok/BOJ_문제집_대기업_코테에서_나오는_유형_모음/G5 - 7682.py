def is_finished(winner):
    key = winner * 3

    # 행 검사
    if key in [''.join(row) for row in board]:
        return True

    # 열 검사
    if key in [''.join([row[i] for row in board]) for i in range(3)]:
        return True

    # 대각선 검사
    if key in [''.join([board[i][i] for i in range(3)]), ''.join([board[j][abs(j - 2)] for j in range(3)])]:
        return True

    return False


def is_valid(x, o):
    if (x > 5) or (o > 4):
        print("invalid")
        return
    valid = False
    of, xf = is_finished("O"), is_finished("X")

    # O 가 마지막에 말을 둔 상황 -> O가 이겨야 함
    if x == o:
        if of and (not xf):
            valid = True
    # X가 마지막에 둔 상황 -> X가 이기거나, 비긴 상황(칸이 다 채워졌을때)
    elif x == (o + 1):
        if xf and (not of):
            valid = True
        elif (not of) and (not xf):
            if x + o == 9:
                valid = True
    if valid:
        print("valid")
    else:
        print("invalid")

while True:
    board = input().rstrip()
    if board == "end": break

    X_cnt, O_cnt = board.count("X"), board.count("O")

    board = [list(board[i:i + 3]) for i in range(0, 7, 3)]
    is_valid(X_cnt, O_cnt)