from collections import deque

N = int(input())
board = list()

shark_x, shark_y = 0, 0

for y_idx in range(N):
    y_board = list(map(int, input().split()))
    for x_idx in range(N):
        if y_board[x_idx] == 9:
            # 아기 상어 위치
            y_board[x_idx] = 0
            shark_x, shark_y = x_idx, y_idx  # 상어 좌표

    board.append(y_board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

baby_size = 2
now_eat = 0

dq = deque()

while True:
    # 먹을 수 있는 물고기 조사
    dq.append([shark_x, shark_y, 0])

    # 거리, y 좌표, x 좌표
    eatable_fish_list = []

    visited = [[-1] * N for _ in range(N)]
    visited[shark_y][shark_x] = 0
    while dq:
        now_x, now_y, now_distance = dq.popleft()

        new_distance = now_distance + 1

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < N) or not(0 <= new_y < N):
                continue

            # 이미 방문 했다면,
            if visited[new_y][new_x] != -1:
                continue

            # 나보다 크기가 크면 못지나감
            if board[new_y][new_x] > baby_size:
                continue

            # 먹을 수 있는 상어인지 확인
            if 0 < board[new_y][new_x] < baby_size:
                eatable_fish_list.append([new_distance, new_y, new_x])

            visited[new_y][new_x] = new_distance
            dq.append([new_x, new_y, new_distance])

    # 먹을 수 있는 상어가 없다면,
    if len(eatable_fish_list) == 0:
        break

    # 먹을 물고기 정하기
    eatable_fish_list.sort()
    eat_fish = eatable_fish_list[0]
    answer += eat_fish[0]

    # 물고기 먹음
    board[eat_fish[1]][eat_fish[2]] = 0
    shark_x, shark_y = eat_fish[2], eat_fish[1]
    now_eat += 1

    # 상어 몸집 키울 수 있는지 확인
    if now_eat == baby_size:
        baby_size += 1
        now_eat = 0

print(answer)


