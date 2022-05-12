def rotate(board, m, n):
    # 제일 윗 줄
    temp = board[0][-1]
    board[0][1:] = board[0][0:-1]
    board[0][0] = board[1][0]

    for i in range(1, n-1):
        temp2 = board[i][-1]
        board[i][-1] = temp
        temp = temp2
        board[i][0] = board[i+1][0]

    # 가장 마지막 줄
    board[-1][0:-1] = board[-1][1:]
    board[-1][-1] = temp

    return board


def shiftRow(board, m, n):
    temp = board[-1]

    for i in range(n-1, 0, -1):
        board[i] = board[i-1]

    board[0] = temp

    return board


def solution(board, operations):
    # 세로, 가로
    n, m = len(board), len(board[0])
    for o in operations:
        if o == "Rotate":
            board = rotate(board, m, n)
        elif o == "ShiftRow":
            board = shiftRow(board, m, n)
    print(board)


solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"])
solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"])
solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])
