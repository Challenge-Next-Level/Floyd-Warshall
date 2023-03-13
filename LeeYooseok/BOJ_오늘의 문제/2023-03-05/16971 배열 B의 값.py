N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
# 교환하지 않은 상태
for _y in range(N):
    temp_sum = (board[_y][0] + board[_y][M - 1])
    temp_sum += (2 * sum(board[_y][1:M - 1]))
    if _y == 0 or _y == N - 1:
        answer += temp_sum
    else:
        answer += 2 * temp_sum

# 행 교환
if N > 2:
    # 교환할 행 찾기
    init_row_sum = board[0][0] + board[0][M - 1] + 2 * sum(board[0][1:M - 1])
    end_row_sum = board[N - 1][0] + board[N - 1][M - 1] + 2 * sum(board[N - 1][1:M - 1])
    change_outer_row = 0
    if init_row_sum < end_row_sum:
        change_outer_row = N - 1

    min_row_sum = 1e9
    change_inner_row = 0
    for r in range(1, N - 1):
        inner_row_sum = board[r][0] + board[r][M - 1] + 2 * sum(board[r][1:M - 1])
        if min_row_sum > inner_row_sum:
            min_row_sum = inner_row_sum
            change_inner_row = r

    # 교환
    row_sum = 0
    for _y in range(N):
        temp_sum = (board[_y][0] + board[_y][M - 1])
        temp_sum += (2 * sum(board[_y][1:M - 1]))
        if _y == 0 or _y == N - 1:
            if _y == change_outer_row:
                row_sum += 2 * temp_sum
            else:
                row_sum += temp_sum
        else:
            if _y == change_inner_row:
                row_sum += temp_sum
            else:
                row_sum += 2 * temp_sum
    answer = max(row_sum, answer)

# 열 교환
if M > 2:
    transpose_board = list(map(list, zip(*board)))
    # 교환할 행 찾기
    init_row_sum = transpose_board[0][0] + transpose_board[0][N - 1] + 2 * sum(transpose_board[0][1:N - 1])
    end_row_sum = transpose_board[M - 1][0] + transpose_board[M - 1][N - 1] + 2 * sum(transpose_board[M - 1][1:N - 1])
    change_outer_row = 0
    if init_row_sum < end_row_sum:
        change_outer_row = M - 1

    min_row_sum = 1e9
    change_inner_row = 0
    for r in range(1, M - 1):
        inner_row_sum = transpose_board[r][0] + transpose_board[r][N - 1] + 2 * sum(transpose_board[r][1:N - 1])
        if min_row_sum > inner_row_sum:
            min_row_sum = inner_row_sum
            change_inner_row = r

    # 교환
    row_sum = 0
    for _y in range(M):
        temp_sum = (transpose_board[_y][0] + transpose_board[_y][N - 1])
        temp_sum += (2 * sum(transpose_board[_y][1:N - 1]))
        if _y == 0 or _y == M - 1:
            if _y == change_outer_row:
                row_sum += 2 * temp_sum
            else:
                row_sum += temp_sum
        else:
            if _y == change_inner_row:
                row_sum += temp_sum
            else:
                row_sum += 2 * temp_sum
    answer = max(row_sum, answer)

print(answer)

