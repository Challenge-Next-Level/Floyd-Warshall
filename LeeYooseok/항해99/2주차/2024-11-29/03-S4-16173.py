import sys

input = sys.stdin.readline

from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

visited = [[False for _ in range(N)] for _ in range(N)]


queue = deque([[0, 0]])
visited[0][0] = True

answer = False

while queue:
    now_x, now_y = queue.popleft()

    if now_x == N - 1 and now_y == N - 1:
        answer = True
        break

    move_cnt = board[now_y][now_x]

    for i in range(2):
        new_x, new_y = now_x + move_cnt * dx[i], now_y + move_cnt * dy[i]

        if not (0 <= new_x < N) or not (0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        visited[new_y][new_x] = True
        queue.append([new_x, new_y])

if answer:
    print("HaruHaru")
else:
    print("Hing")