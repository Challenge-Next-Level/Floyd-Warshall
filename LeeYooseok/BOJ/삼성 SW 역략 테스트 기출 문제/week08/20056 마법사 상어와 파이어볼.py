N, M, K = map(int, input().split())

# 방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# N x N 격자 : 각 칸에 [[질략, 속력, 방향], [질략, 속력, 방향]]
board = [[[] for _ in range(N)] for _ in range(N)]

# ball 위치 x,y
ball_loc_list = list()

for _ in range(M):
    # y, x - 1부터 시작
    y, x, m, s, d = map(int, input().split())
    board[y-1][x-1].append([m, s, d])
    ball_loc_list.append([x-1, y-1])
# K번 명령 수행
for k in range(K):

    new_board = [[[] for _ in range(N)] for _ in range(N)]
    new_ball_list = set()
    # ball 이동
    for x, y in ball_loc_list:
        for ball in board[y][x]:
            old_m, old_s, old_d = ball
            new_x, new_y = (x + old_s * dx[old_d]) % N, (y + old_s * dy[old_d]) % N

            new_board[new_y][new_x].append([old_m, old_s, old_d])
            new_ball_list.add((new_x, new_y))
    new_new_ball_list = set()
    # ball 합치고 나누기
    for x, y in new_ball_list:
        # 2개 이상이면
        if len(new_board[y][x]) > 1:
            temp_list = [0, 0]
            r_flag = True
            if new_board[y][x][0][2] % 2 == 0:
                d_flag = True
            else:
                d_flag = False

            for ball_info in new_board[y][x]:
                temp_list[0] += ball_info[0]
                temp_list[1] += ball_info[1]
                if ball_info[2] % 2 == 0:
                    b_d = True
                else:
                    b_d = False
                if r_flag:
                    if d_flag != b_d:
                        r_flag = False

            new_m, new_s = temp_list[0] // 5, temp_list[1] // len(new_board[y][x])
            if r_flag:
                new_d = [0, 2, 4, 6]
            else:
                new_d = [1, 3, 5, 7]

            new_board[y][x] = []
            if new_m == 0:
                continue
            new_new_ball_list.add((x, y))
            for i in range(4):
                new_board[y][x].append([new_m, new_s, new_d[i]])
        else:
            new_new_ball_list.add((x, y))
    ball_loc_list = list(new_new_ball_list)
    board = new_board


result = 0
for x, y in ball_loc_list:
    for ball in board[y][x]:
        result += ball[0]

print(result)






