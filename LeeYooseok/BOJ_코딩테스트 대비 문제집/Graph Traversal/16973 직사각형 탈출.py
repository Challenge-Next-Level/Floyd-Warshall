import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = list()
wall_list = list()

for y in range(N):
    y_board = list(map(int, input().split()))
    for x in range(M):
        if y_board[x] == 1:
            wall_list.append([x, y])
    board.append(y_board)

visited = [[False for _ in range(M)] for _ in range(N)]

H, W, S_R, S_C, F_R, F_C = map(int, input().split())

def check(square_x, square_y):
    for w_x, w_y in wall_list:
        if square_x <= w_x < square_x + W and square_y <= w_y < square_y + H:
            return False
    return True


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()
que.append([S_C - 1, S_R - 1, 0])
visited[S_R - 1][S_C - 1] = True

while que:
    now_x, now_y, now_t = que.popleft()

    if now_x == F_C - 1 and now_y == F_R - 1:
        print(now_t)
        exit()

    new_t = now_t + 1
    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        # 직사각형 범위 벗어나는지 확인
        if not (0 <= new_x) or not (0 <= new_y) or not (new_x + W - 1 < M) or not (new_y + H - 1 < N):
            continue

        if visited[new_y][new_x]:
            continue

        # 직사각형 범위에 벽이 있는지 확인
        if not check(new_x, new_y):
            continue

        que.append([new_x, new_y, new_t])
        visited[new_y][new_x] = True

print(-1)
