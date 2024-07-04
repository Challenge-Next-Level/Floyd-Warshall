N = int(input())
board = list()
answer = [0, 0]
for _ in range(N):
    x_board = input()
    space_cnt = 0
    check = True
    for x in x_board:
        if x == ".":
            space_cnt += 1
        else:
            space_cnt = 0
            if not check:
                check = True
        if space_cnt >= 2 and check:
            answer[0] += 1
            check = False
    board.append(x_board)

for _x in range(N):
    space_cnt = 0
    check = True
    for _y in range(N):
        if board[_y][_x] == ".":
            space_cnt += 1
        else:
            space_cnt = 0
            if not check:
                check = True
        if space_cnt >= 2 and check:
            answer[1] += 1
            check = False

print(*answer)