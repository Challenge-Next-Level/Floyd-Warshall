import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

while N != 1:
    temp_N = N // 2
    temp_board = [[0 for _ in range(temp_N)] for _ in range(temp_N)]

    for _y in range(0, N, 2):
        for _x in range(0, N, 2):
            num_list = [board[_y][_x], board[_y][_x + 1], board[_y + 1][_x], board[_y + 1][_x + 1]]
            num_list.sort()
            temp_board[_y // 2][_x // 2] = num_list[1]

    board = temp_board
    N = temp_N

print(board[0][0])