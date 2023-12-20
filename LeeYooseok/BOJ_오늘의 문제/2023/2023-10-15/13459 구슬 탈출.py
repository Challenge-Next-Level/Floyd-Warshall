from collections import deque

N, M = map(int, input().split())
board = list()

red_loc = [0, 0]
blue_loc = [0, 0]
for _y in range(N):
    x_board = list(input())
    for _x in range(M):
        if x_board[_x] == 'R':
            red_loc = [_x, _y]
        if x_board[_x] == 'B':
            blue_loc = [_x, _y]
    board.append(x_board)

# 빨강 구슬만 있을 경우,
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([[red_loc[0], red_loc[1], blue_loc[0], blue_loc[1], 0]])
visited = list()
visited.append([red_loc[0], red_loc[1], blue_loc[0], blue_loc[1]])

while queue:
    now_red_x, now_red_y, now_blue_x, now_blue_y, now_cnt = queue.popleft()

    # 10회 이상 움직였다면,
    if now_cnt > 10:
        print(0)
        exit()

    # 10회 안에 구멍에 들어갔다면
    if board[now_red_y][now_red_x] == 'O':
        print(1)
        exit()

    for i in range(4):
        # 빨강색 움직임
        new_red_x, new_red_y, red_move_cnt = now_red_x, now_red_y, 0
        while True:
            new_red_x, new_red_y, red_move_cnt = new_red_x + dx[i], new_red_y + dy[i], red_move_cnt + 1

            if board[new_red_y][new_red_x] == '#':
                new_red_x, new_red_y = new_red_x - dx[i], new_red_y - dy[i]
                red_move_cnt -= 1
                break

            if board[new_red_y][new_red_x] == 'O':
                break

        # 파랑색 움직임
        new_blue_x, new_blue_y, blue_move_cnt = now_blue_x, now_blue_y, 0
        while True:
            new_blue_x, new_blue_y, blue_move_cnt = new_blue_x + dx[i], new_blue_y + dy[i], blue_move_cnt + 1

            if board[new_blue_y][new_blue_x] == '#':
                new_blue_x, new_blue_y = new_blue_x - dx[i], new_blue_y - dy[i]
                blue_move_cnt -= 1
                break

            if board[new_blue_y][new_blue_x] == 'O':
                break

        # 파랑색 공이 구멍에 들어가면 무시
        if board[new_blue_y][new_blue_x] == 'O':
            continue

        # 빨강 파랑이 같은 위치라면
        if new_red_x == new_blue_x and new_red_y == new_blue_y:
            # 더 많이 이동한 구슬이 더 늦게 도착한 것
            if red_move_cnt > blue_move_cnt:
                new_red_x, new_red_y = new_red_x - dx[i], new_red_y - dy[i]
            else:
                new_blue_x, new_blue_y = new_blue_x - dx[i], new_blue_y - dy[i]

        # queue 에 추가
        if [new_red_x, new_red_y, new_blue_x, new_blue_y] not in visited:
            queue.append([new_red_x, new_red_y, new_blue_x, new_blue_y, now_cnt + 1])
            visited.append([new_red_x, new_red_y, new_blue_x, new_blue_y])

# 10회를 초과하지 않아도 구멍에 못들어가는 경우
print(0)