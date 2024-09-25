def solution(m, n, puddles):
    
    board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for puddle in puddles:
        board[puddle[1]][puddle[0]] = -1

    board[1][1] = 1

    for _y in range(1, n + 1):
        for _x in range(1, m + 1):
            if board[_y][_x] == -1:
                continue

            if board[_y - 1][_x] != -1:
                board[_y][_x] += board[_y - 1][_x]

            if board[_y][_x - 1] != -1:
                board[_y][_x] += board[_y][_x - 1]

            board[_y][_x] %= 1000000007

    return board[-1][-1]