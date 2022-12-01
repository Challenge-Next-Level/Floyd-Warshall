N = int(input())

board = [list(map(int, list(input()))) for _ in range(N)]


def solve(_board, _n):
    chk = _board[0][0]
    for y_board in _board:
        for b in y_board:
            if chk != b:
                chk = -1
                break

    if chk == -1:
        print("(", end='')
        _n = _n // 2

        solve([item[0:_n] for item in _board[0:_n]], _n)
        solve([item[_n:2 * _n] for item in _board[0:_n]], _n)
        solve([item[0:_n] for item in _board[_n:2 * _n]], _n)
        solve([item[_n:2 * _n] for item in _board[_n:2 * _n]], _n)
        print(")", end='')
    elif chk == 1:
        print(1, end='')
    else:
        print(0, end='')


solve(board, N)
