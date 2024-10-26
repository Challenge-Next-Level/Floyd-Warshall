import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 바라볼 수 있는 방향 리스트 [dx, dy]
cctv_direct_list = [[],
                    [[[-1, 0]], [[1, 0]], [[0, -1]], [[0, 1]]],
                    [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
                    [[[1, 0], [0, -1]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]], [[0, 1], [1, 0]]],
                    [[[1, 0], [0, -1], [-1, 0]], [[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]]],
                    [[[1, 0], [0, -1], [-1, 0], [0, 1]]]]

board = list()
cctv_list = list()
empty_space = 0
answer = 1e9
for _y in range(N):
    x_board = list(map(int, input().split()))
    for _x in range(M):
        if 1 <= x_board[_x] <= 5:
            cctv_list.append([x_board[_x], [_x, _y]])
        elif x_board[_x] == 0:
            empty_space += 1

    board.append(x_board)

board_copy = [data[:] for data in board]


def install_cctv(cctv_idx, check_board, cover_cnt):
    global answer

    # 종료 조건
    if cctv_idx == len(cctv_list):
        answer = min(answer, empty_space - cover_cnt)
        return

    cctv_type, cctv_loc = cctv_list[cctv_idx]

    cctv_x, cctv_y = cctv_loc

    for cctv_direct in cctv_direct_list[cctv_type]:
        next_board = [data[:] for data in check_board]
        now_cover_cnt = 0

        for dx, dy in cctv_direct:
            cover_x, cover_y = cctv_x, cctv_y

            while True:
                cover_x, cover_y = cover_x + dx, cover_y + dy

                if not (0 <= cover_x < M) or not (0 <= cover_y < N):
                    break

                if board[cover_y][cover_x] == 6:
                    break

                if board[cover_y][cover_x] == 0 and next_board[cover_y][cover_x] != "#":
                    next_board[cover_y][cover_x] = "#"
                    now_cover_cnt += 1

        install_cctv(cctv_idx + 1, next_board, cover_cnt + now_cover_cnt)


install_cctv(0, board_copy, 0)

print(answer)
