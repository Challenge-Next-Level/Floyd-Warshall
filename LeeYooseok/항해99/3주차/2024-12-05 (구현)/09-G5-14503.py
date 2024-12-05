import sys

input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

answer = 0
queue = deque(list())

queue.append([c, r, d])

while queue:
    now_x, now_y, now_dir = queue.popleft()
    # 현재 칸이 아직 청소되어 있지 않은 경우,
    if board[now_y][now_x] == 0:
        # 현재 칸을 청소한다.
        board[now_y][now_x] = -1
        answer += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    not_clean_count = 0
    for i in range(4):
        next_x, next_y = now_x + dx[i], now_y + dy[i]

        if board[next_y][next_x] == 0:
            not_clean_count += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    if not_clean_count == 0:
        # 바라보는 방향을 유지한 채로 한 칸 후진 위치
        back_x, back_y = now_x - dx[now_dir], now_y - dy[now_dir]

        # 후진할 수 없다면, 작동을 멈춘다.
        if not(1 <= back_x < M - 1) or not(1 <= back_y < N - 1):
            print(answer)
            exit()

        if board[back_y][back_x] == 1:
            print(answer)
            exit()

        queue.append([back_x, back_y, now_dir])

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반 시계 방향으로 90도 회전한다.
        for i in range(1, 5):
            next_dir = (now_dir - i) % 4

            next_x, next_y = now_x + dx[next_dir], now_y + dy[next_dir]

            if not(1 <= next_x < M - 1) or not(1 <= next_y < N - 1):
                continue

            if board[next_y][next_x] != 0:
                continue

            queue.append([next_x, next_y, next_dir])
            break



