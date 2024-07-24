M, N = map(int, input().split())
board = list([0 for _ in range(N)] for _ in range(M))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

now_loc = [0, 0]
board[0][0] = 1
visit_cnt = 1

now_dir = 0

answer = 0

while visit_cnt != (M * N):
    new_x, new_y = now_loc[0] + dx[now_dir], now_loc[1] + dy[now_dir]

    if (not(0 <= new_x < N) or not(0 <= new_y < M)) or board[new_y][new_x] == 1:
        now_dir = (now_dir + 1) % 4
        new_x, new_y = now_loc[0] + dx[now_dir], now_loc[1] + dy[now_dir]
        answer += 1

    board[new_y][new_x] = 1
    visit_cnt += 1
    now_loc = [new_x, new_y]

print(answer)
