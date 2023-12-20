N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    temp_array = [item[:] for item in board]

    # 밖에서부터 돌리기
    for idx in range(min(M, N) // 2):
        # 구간 시작과 끝
        s_x, s_y, e_x, e_y = idx, idx, M - 1 - idx, N - 1 - idx

        # 위, 아래
        for i in range(s_x, e_x):
            temp_array[s_y][i] = board[s_y][i + 1]
            temp_array[e_y][i + 1] = board[e_y][i]

        # 오른쪽, 왼쪽
        for i in range(s_y, e_y):
            temp_array[i][e_x] = board[i + 1][e_x]
            temp_array[i + 1][s_x] = board[i][s_x]

    board = [item[:] for item in temp_array]

for b in board:
    print(" ".join(list(map(str, b))))