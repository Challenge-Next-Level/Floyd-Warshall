from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

score = 0


# 중력 - 열 기준 맨 밑에서부터 내린다.
def Z(input_board):
    for z_x in range(N):
        for z_y in range(N - 1, -1, -1):
            # 일반 또는 무지개 블럭만 내려감
            if input_board[z_y][z_x] >= 0:
                now_z_y = z_y
                while True:
                    # 가장 위부터, 가장 밑의 윗부분 즉 내릴 수 있는 공간이 있다면
                    if 0 <= now_z_y + 1 < N:
                        # 밑의 공간이 비어있다면
                        if input_board[now_z_y + 1][z_x] == -2:
                            # 값 변경
                            input_board[now_z_y + 1][z_x] = input_board[now_z_y][z_x]
                            input_board[now_z_y][z_x] = -2
                            # 한칸 아래로 pointer 이동
                            now_z_y += 1
                        else:
                            break
                    else:
                        break
    return input_board


while True:
    # 가장 큰 블록 그룹을 찾는다.
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # block - 크기, 무지개 블록의 개수, 기준 블록의 행, 기준 블록의 열
    big_block = [0, 0, 0, 0]
    for _y in range(N):
        for _x in range(N):
            # 방문하지 않았어야 하고, 일반 블록이 적어도 하나 들어있어야 한다.
            if visited[_y][_x] != 1 and board[_y][_x] > 0:
                # 0 중복 이동 가능하기 때문에 block 별로 처리
                now_visited = [[0 for _ in range(N)] for _ in range(N)]
                # 크기, 무지개 블록의 개수
                size = 1
                muzi = 0
                # 블록 행, 열
                queue = deque([[_y, _x]])
                visited[_y][_x] = 1
                now_visited[_y][_x] = 1
                # 일반 블럭 색
                now_color = board[_y][_x]

                while queue:
                    y, x = queue.popleft()

                    for d in range(4):
                        n_y, n_x = y + dy[d], x + dx[d]
                        # 격자 판 벗어나는지 확인
                        if not (0 <= n_y < N) or not (0 <= n_x < N):
                            continue

                        # 현재 일반 블럭 색상과 같거나, 무지개 블럭과 같거나
                        if board[n_y][n_x] != now_color and board[n_y][n_x] != 0:
                            continue

                        # 검은색 블록은 포함 x, 빈공간 포함 x
                        if board[n_y][n_x] < 0:
                            continue

                        # 방문 확인 but, 무지개 블럭은 포함될 수 있도록 한다.
                        if now_visited[n_y][n_x] == 1:
                            continue

                        if board[n_y][n_x] == 0:
                            muzi += 1

                        queue.append([n_y, n_x])
                        visited[n_y][n_x] = 1
                        now_visited[n_y][n_x] = 1
                        size += 1

                # big_block 갱신
                if size >= 2:
                    if big_block[0] < size:
                        big_block = [size, muzi, _y, _x]
                    elif big_block[0] == size:
                        if big_block[1] < muzi:
                            big_block = [size, muzi, _y, _x]
                        elif big_block[1] == muzi:
                            if big_block[2] < _y:
                                big_block = [size, muzi, _y, _x]
                            elif big_block[2] == _y:
                                if big_block[3] < _x:
                                    big_block = [size, muzi, _y, _x]

    # block 그룹이 존재하지 않으면
    if big_block[0] < 2:
        print(score)
        break

    # 찾은 블록 그룹을 제거한다.
    get_score = 0
    block_size, block_muzi, block_y, block_x = big_block
    now_color = board[block_y][block_x]
    queue = deque([[block_y, block_x]])

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[block_y][block_x] = 1

    while queue:
        now_y, now_x = queue.popleft()
        get_score += 1
        # block 제거
        board[now_y][now_x] = -2

        for d in range(4):
            new_y, new_x = now_y + dy[d], now_x + dx[d]

            if not (0 <= new_y < N) or not (0 <= new_x < N):
                continue

            # 현재 일반 블럭 색상과 같아야 하고, 검은색 블록은 포함 x, 빈공간 포함 x
            if board[new_y][new_x] != now_color and board[new_y][new_x] != 0:
                continue

            if board[new_y][new_x] < 0:
                continue

            # 방문 확인
            if visited[new_y][new_x] == 1:
                continue

            queue.append([new_y, new_x])
            visited[new_y][new_x] = 1
    score += (get_score ** 2)

    # 중력 - 열 기준 맨 밑에서부터 내린다.
    board = Z(board)


    # 90도 반시계 방향 회전
    # new_board = [[0 for _ in range(N)] for _ in range(N)]
    # for r_x in range(N):
    #     for r_y in range(N-1, -1, -1):
    #         new_board[N-1 - r_x][r_y] = board[r_y][r_x]
    # board = [item[:] for item in new_board]
    # 90도 반시계 방향
    new_board = list(zip(*board))
    new_board.reverse()
    for i in range(N):
        board[i] = list(new_board[i])

    # 중력 - 열 기준 맨 밑에서부터 내린다.
    board = Z(board)
