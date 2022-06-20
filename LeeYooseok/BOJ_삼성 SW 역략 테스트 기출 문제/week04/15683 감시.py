import sys

n, m = map(int, input().split())
board = list()

# x, y, 번호
cctv_list = list()

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] > 0:
            cctv_list.append([j, i, temp[j]])
    board.append(temp)

num_cctv = len(cctv_list)

result = sys.maxsize


def check(cnt, board):
    global result
    if cnt == num_cctv:
        temp = 0
        for b in board:
            temp += b.count(0)
        result = min(result, temp)
        return

    now_cctv = cctv_list[cnt]


    # 한방향
    if now_cctv[2] == 1:
        for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            temp_board = [item[:] for item in board]
            new_x, new_y = now_cctv[0] + dx, now_cctv[1] + dy
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + dx, new_y + dy
            check(cnt + 1, temp_board)
    # 양 끝
    elif now_cctv[2] == 2:
        for d in [[[1, 0], [-1, 0]], [[0, -1], [0, 1]]]:
            temp_board = [item[:] for item in board]

            new_x, new_y = now_cctv[0] + d[0][0], now_cctv[1] + d[0][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[0][0], new_y + d[0][1]

            new_x, new_y = now_cctv[0] + d[1][0], now_cctv[1] + d[1][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[1][0], new_y + d[1][1]

            check(cnt + 1, temp_board)

    # 직각 방향
    elif now_cctv[2] == 3:
        for d in [[[1, 0], [0, -1]], [[1, 0], [0, 1]], [[-1, 0], [0, -1]], [[-1, 0], [0, 1]]]:
            temp_board = [item[:] for item in board]

            new_x, new_y = now_cctv[0] + d[0][0], now_cctv[1] + d[0][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[0][0], new_y + d[0][1]

            new_x, new_y = now_cctv[0] + d[1][0], now_cctv[1] + d[1][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[1][0], new_y + d[1][1]

            check(cnt + 1, temp_board)

    # 세 방향
    elif now_cctv[2] == 4:
        for d in [[[1, 0], [0, -1], [0, 1]], [[-1, 0], [0, -1], [0, 1]], [[0, 1], [1, 0], [-1, 0]],
                  [[0, -1], [1, 0], [-1, 0]]]:
            temp_board = [item[:] for item in board]

            new_x, new_y = now_cctv[0] + d[0][0], now_cctv[1] + d[0][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[0][0], new_y + d[0][1]

            new_x, new_y = now_cctv[0] + d[1][0], now_cctv[1] + d[1][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[1][0], new_y + d[1][1]

            new_x, new_y = now_cctv[0] + d[2][0], now_cctv[1] + d[2][1]
            while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
                if board[new_y][new_x] == 0:
                    temp_board[new_y][new_x] = '#'
                new_x, new_y = new_x + d[2][0], new_y + d[2][1]

            check(cnt + 1, temp_board)

    # 네 방향
    elif now_cctv[2] == 5:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        temp_board = [item[:] for item in board]

        new_x, new_y = now_cctv[0] + d[0][0], now_cctv[1] + d[0][1]
        while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
            if board[new_y][new_x] == 0:
                temp_board[new_y][new_x] = '#'
            new_x, new_y = new_x + d[0][0], new_y + d[0][1]

        new_x, new_y = now_cctv[0] + d[1][0], now_cctv[1] + d[1][1]
        while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
            if board[new_y][new_x] == 0:
                temp_board[new_y][new_x] = '#'
            new_x, new_y = new_x + d[1][0], new_y + d[1][1]

        new_x, new_y = now_cctv[0] + d[2][0], now_cctv[1] + d[2][1]
        while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
            if board[new_y][new_x] == 0:
                temp_board[new_y][new_x] = '#'
            new_x, new_y = new_x + d[2][0], new_y + d[2][1]

        new_x, new_y = now_cctv[0] + d[3][0], now_cctv[1] + d[3][1]
        while 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != 6:
            if board[new_y][new_x] == 0:
                temp_board[new_y][new_x] = '#'
            new_x, new_y = new_x + d[3][0], new_y + d[3][1]

        check(cnt + 1, temp_board)

    elif now_cctv[2] == 6:
        check(cnt + 1, board)


check(0, board)

print(result)
