R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

temp_board = [item[:] for item in board]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_x, min_y, max_x, max_y = C-1, R-1, 0, 0

for r in range(R):
    for c in range(C):
        if board[r][c] == 'X':
            ocean = 0
            for i in range(4):
                new_r, new_c = r + dy[i], c + dx[i]

                if 0 <= new_c < C and 0 <= new_r < R:
                    if board[new_r][new_c] == '.':
                        ocean += 1
                else:
                    ocean += 1

            # 인접한 세칸 또는 네 칸에 바다가 있다면,
            if ocean >= 3:
                temp_board[r][c] = '.'
            else:
                min_x = min(min_x, c)
                min_y = min(min_y, r)
                max_x = max(max_x, c)
                max_y = max(max_y, r)

for _y in range(min_y, max_y + 1):
    print("".join(temp_board[_y][min_x:max_x+1]))


