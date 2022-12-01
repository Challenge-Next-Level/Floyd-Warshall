# zero_position : 초기 pop 으로 구현 -> idx 활용
# board 값 변경 후 다시 0으로 변경 필요

zero_position = list()
board = list()
for _y in range(9):
    y_board = list(map(int, input().split()))
    for _x in range(9):
        if y_board[_x] == 0:
            zero_position.append([_x, _y])
    board.append(y_board)

zero_len = len(zero_position)

def check(zero_idx):
    # 모든 0을 다 채웠다면?
    if zero_idx == zero_len:
        for b in board:
            print(" ".join(map(str, b)))
        exit()

    z_x, z_y = zero_position[zero_idx]

    num_list = set([n for n in range(1, 10)])
    # 가로
    for xx in range(0, 9):
        if board[z_y][xx] != 0 and board[z_y][xx] in num_list:
            num_list.remove(board[z_y][xx])
    # 세로
    for yy in range(0, 9):
        if board[yy][z_x] != 0 and board[yy][z_x] in num_list:
            num_list.remove(board[yy][z_x])
    # 3 X 3
    xxx, yyy = (z_x // 3) * 3, (z_y // 3) * 3
    for xxxx in range(xxx, xxx + 3):
        for yyyy in range(yyy, yyy + 3):
            if board[yyyy][xxxx] != 0 and board[yyyy][xxxx] in num_list:
                num_list.remove(board[yyyy][xxxx])

    # num_list 에 있는 수를 채워서 다음 함수 실행
    for num in num_list:
        board[z_y][z_x] = num
        check(zero_idx + 1)
        board[z_y][z_x] = 0


check(0)
