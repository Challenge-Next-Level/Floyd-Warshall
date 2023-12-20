import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
board = list()

start_loc = list()
for _y in range(4 * k):
    x_board = list(input())
    for _x in range(4 * k):
        if x_board[_x] == 'S':
            start_loc = [_x, _y, 0]
            x_board[_x] = "."
    board.append(x_board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# d 만큼 회전한 후의 x, y 까지 방문 하는데 걸리는 횟수
visited = [[[-1, -1, -1, -1] for _ in range(4 * k)] for _ in range(4 * k)]
visited[start_loc[1]][start_loc[0]][0] = 0


def rotate_board(_board, rot_x, rot_y, now_d):
    rotated_board = [item[:] for item in _board]

    rot_s_x, rot_s_y = (rot_x // 4) * 4, (rot_y // 4) * 4

    if now_d == 1:
        # rotate 90
        for r_x in range(4):
            for r_y in range(4):
                rotated_board[r_x + rot_s_y][4 - 1 - r_y + rot_s_x] = board[r_y + rot_s_y][r_x + rot_s_x]
    elif now_d == 2:
        # rotate 180
        for r_x in range(4):
            for r_y in range(4):
                rotated_board[4 - 1 - r_y + rot_s_y][4 - 1 - r_x + rot_s_x] = board[r_y + rot_s_y][r_x + rot_s_x]
    elif now_d == 3:
        # rotate 270
        for r_x in range(4):
            for r_y in range(4):
                rotated_board[4 - 1 - r_x + rot_s_y][r_y + rot_s_x] = board[r_y + rot_s_y][r_x + rot_s_x]
    return rotated_board


def rotate_loc(origin_x, origin_y):

    rot_start_x, rot_start_y = (origin_x // 4) * 4, (origin_y // 4) * 4

    return rot_start_x + (4 - 1 - (origin_y - rot_start_y)), rot_start_y + (origin_x - rot_start_x)


que = deque([start_loc])

while que:
    # 회전한 후의 위치, 회전 수
    now_x, now_y, now_d = que.popleft()
    now_cnt = visited[now_y][now_x][now_d] # 해당 위치에 now_d 번 회전한 경우까지 도달한 라운드 수

    # 현재 있는 구역만 now_d 만큼 시계방향으로 회전한다.
    temp_board = rotate_board(board, now_x, now_y, now_d)

    if temp_board[now_y][now_x] == 'E':
        print(now_cnt)
        exit()

    # 1. 상하좌우로 이동하거나,
    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        # 단, 이동할 곳에 벽이 있거나 미로를 벗어나는 곳이면 이동하지 못한다.
        if not (0 <= new_x < 4 * k) or not (0 <= new_y < 4 * k):
            continue

        if temp_board[new_y][new_x] == '#':
            continue

        # 1번이 끝나고 현재 서 있는 위치 (y, x)가 포함된 구역이 시계방향으로 90도 회전한다.
        rotated_x, rotated_y = rotate_loc(new_x, new_y)

        # 이동하기 전에 있는 구역과 같은 구역이라면,
        if ((now_x // 4) * 4 == (rotated_x // 4) * 4) and ((now_y // 4) * 4 == (rotated_y // 4) * 4):
            new_d = (now_d + 1) % 4
        # 이동하기 전에 있는 구역과 다른 구역이라면,
        else:
            new_d = 1

        # visited update
        if visited[rotated_y][rotated_x][new_d] != -1:
            if visited[rotated_y][rotated_x][new_d] >= now_cnt + 1:
                visited[rotated_y][rotated_x][new_d] = now_cnt + 1

                que.append([rotated_x, rotated_y, new_d])
        else:
            visited[rotated_y][rotated_x][new_d] = now_cnt + 1

            que.append([rotated_x, rotated_y, new_d])

    # 1. 또는 가만히 있는다.
    # 2. 1번이 끝나고 현재 서 있는 위치 (y, x)가 포함된 구역이 시계방향으로 90도 회전한다.
    rotated_now_x, rotated_now_y = rotate_loc(now_x, now_y)
    new_d = (now_d + 1) % 4
    if visited[rotated_now_y][rotated_now_x][new_d] != -1:
        if visited[rotated_now_y][rotated_now_x][new_d] >= now_cnt + 1:
            visited[rotated_now_y][rotated_now_x][new_d] = now_cnt + 1

            # 1번이 끝나고 현재 서 있는 위치 (y, x)가 포함된 구역이 시계방향으로 90도 회전한다.
            que.append([rotated_now_x, rotated_now_y, new_d])
    else:
        visited[rotated_now_y][rotated_now_x][new_d] = now_cnt + 1

        # 1번이 끝나고 현재 서 있는 위치 (y, x)가 포함된 구역이 시계방향으로 90도 회전한다.
        que.append([rotated_now_x, rotated_now_y, new_d])

print(-1)