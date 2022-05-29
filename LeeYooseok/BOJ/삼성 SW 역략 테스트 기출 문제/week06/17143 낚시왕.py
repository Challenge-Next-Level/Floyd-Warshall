# y, x -> R, C

R, C, M = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 행, 열 위치 바꿔서 관리할것 임
shark_board = [[[] for _ in range(R)] for _ in range(C)]

# 현재 낚시왕의 위치
fisher_man = -1

# 낚시왕이 잡은 물고기 크기
result = 0

# 상어 위치
shark_list = list()

# 상어의 정보 입력
for _ in range(M):
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
    # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
    r, c, s, d, z = list(map(int, input().split()))

    shark_board[c-1][r-1] = [z, s, d-1]
    shark_list.append([c-1, r-1])


while fisher_man < C - 1 and shark_list:
    # 1) 낚시왕이 오른쪽으로 한 칸 이동한다.
    fisher_man += 1

    # 2) 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for i in range(R):
        if shark_board[fisher_man][i]:
            result += shark_board[fisher_man][i][0]
            shark_board[fisher_man][i] = []
            break


    # 3) 상어가 이동한다.
    new_shark_board = [[[]] * R for _ in range(C)]
    new_shark_list = list()

    # 상어 리스트 탐색
    # 상어의 위치 - c, r
    for shark in shark_list:
        # 크기, 속력, 이동 방향
        shark_info = shark_board[shark[0]][shark[1]]

        if shark_info:
            dir = shark_info[2]

            now_x, now_y = shark[0], shark[1]
            new_x, new_y = now_x, now_y

            # 위로 이동 | 아래로 이동
            if dir == 0 or dir == 1:
                for d in range(shark_info[1]):
                    new_x, new_y = new_x + dx[dir], new_y + dy[dir]

                    if new_y == R:
                        new_y = R-2
                        dir = 0
                    if new_y == -1:
                        new_y = 1
                        dir = 1

            # 오른쪽 | 왼쪽 이동
            if dir == 2 or dir == 3:
                for d in range(shark_info[1]):
                    new_x, new_y = new_x + dx[dir], new_y + dy[dir],

                    if new_x == C:
                        new_x = C-2
                        dir = 3
                    if new_x == -1:
                        new_x = 1
                        dir = 2

            old_shark = new_shark_board[new_x][new_y]

            if old_shark:
                old_size = old_shark[0]

                if shark_info[0] > old_size:
                    new_shark_board[new_x][new_y] = [shark_info[0], shark_info[1], dir]
            else:
                new_shark_board[new_x][new_y] = [shark_info[0], shark_info[1], dir]

    for c in range(C):
        for r in range(R):
            if new_shark_board[c][r]:
                new_shark_list.append([c, r])

    shark_board = new_shark_board
    shark_list = new_shark_list

print(result)


