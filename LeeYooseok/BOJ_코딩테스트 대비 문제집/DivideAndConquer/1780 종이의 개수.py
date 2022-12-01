N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]  # -1, 0, 1


def solve(_board, _n):
    global result

    # 한 숫자로 있는지 확인
    chk = _board[0][0]

    for b in _board:
        for num in b:
            if chk != num:
                chk = -2
                break

    # 다음 진행
    if chk == -2:
        next_n = _n // 3
        for _y in range(0, _n, next_n):
            for _x in range(0, _n, next_n):
                temp_board = [item[_x: _x + next_n] for item in _board[_y: _y + next_n]]
                solve(temp_board, next_n)
    else:
        result[chk + 1] += 1


solve(board, N)

for r in result:
    print(r)
