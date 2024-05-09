import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    new_board = [b[:] for b in board]
    # 빙산 녺이기
    for _y in range(1, N - 1):
        for _x in range(1, M - 1):
            sub_cnt = 0
            for i in range(4):
                n_y, n_x = _y + dy[i], _x + dx[i]

                if not(0 <= n_x < M) or not(0 <= n_y < N):
                    continue

                if board[n_y][n_x] == 0:
                    sub_cnt += 1

            new_board[_y][_x] = max(board[_y][_x] - sub_cnt, 0)

    board = [nb[:] for nb in new_board]

    # 덩어리 count
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _y in range(1, N - 1):
        for _x in range(1, M - 1):
            if not visited[_y][_x] and board[_y][_x] != 0:
                cnt += 1
                stack = deque([[_x, _y]])
                visited[_y][_x] = True

                while stack:
                    now_x, now_y = stack.pop()

                    for i in range(4):
                        new_x, new_y = now_x + dx[i], now_y + dy[i]

                        if not(0 <= new_x < M) or not(0 <= new_y < N):
                            continue

                        if visited[new_y][new_x]:
                            continue

                        if board[new_y][new_x] > 0:
                            visited[new_y][new_x] = True
                            stack.append([new_x, new_y])

    answer += 1

    if cnt >= 2:
        print(answer)
        exit()

    if cnt == 0:
        print(0)
        exit()