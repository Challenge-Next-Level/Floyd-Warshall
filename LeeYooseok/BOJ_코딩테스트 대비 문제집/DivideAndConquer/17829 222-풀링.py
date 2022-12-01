N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]


def solve(_board, _n):
    if _n == 1:
        print(_board[0][0])
        exit()

    next_n = _n // 2
    next_board = [[0 for _ in range(next_n)] for _ in range(next_n)]

    for _y in range(0, _n, 2):
        for _x in range(0, _n, 2):
            check_board = [item[_x:_x + 2] for item in _board[_y: _y + 2]]

            num_list = check_board[0]
            num_list.extend(check_board[1])

            num_list.sort()

            next_board[_y // 2][_x // 2] = num_list[-2]
    solve(next_board, next_n)

solve(board, N)
